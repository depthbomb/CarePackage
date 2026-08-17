from enum import auto, Enum
from typing import cast, Optional
from PySide6.QtGui import QPixmap
from src.lib.settings import Settings
from src.widgets.spinner import Spinner
from src.lib.software import BaseSoftware
from src import DOWNLOAD_DIR, BROWSER_USER_AGENT
from src.widgets.loading_label import LoadingLabel
from src.enums import SettingsKeys, DownloadTimeout
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest, QNetworkAccessManager
from PySide6.QtWidgets import QLabel, QWidget, QSizePolicy, QHBoxLayout, QProgressBar
from PySide6.QtCore import Slot, QFile, Signal, QTimer, QObject, QProcess, QIODevice, QSaveFile

class SoftwareProgressRow(QWidget):
    class OperationError(Enum):
        NoError = auto()
        DownloadURLResolveError = auto()
        FileDownloadTimeoutError = auto()
        FileDownloadNetworkError = auto()
        FileDownloadIOError = auto()
        InstallationProcessError = auto()
        Canceled = auto()

    url_resolving = Signal()
    url_resolved = Signal(str)
    file_downloading = Signal(str)
    file_downloaded = Signal(QFile)
    installation_requested = Signal()
    finished = Signal(OperationError)

    def __init__(self, software: BaseSoftware, parent: Optional[QObject] = None):
        super().__init__(parent)

        self.probing = False
        self.cancel_requested = False
        self.operation_finished = False
        self.skip_installation = False
        self.install_silently = False
        self.cleanup_postinstall = False

        self.current_bytes = 0
        self.last_bytes = 0
        self.current_speed = 0
        self.formatted_speed = ''

        self.software = software
        self.software.url_resolve_error.connect(self._on_software_download_url_resolve_error_occurred)
        self.software.url_resolved.connect(self._on_software_download_url_resolved)

        self.download_url = cast(Optional[str], None)
        self.download_file = cast(Optional[QFile], None)
        self.download_save_file = cast(Optional[QSaveFile], None)
        self.download_reply = cast(Optional[QNetworkReply], None)
        self.download_write_failed = False
        self.download_timed_out = False
        self.download_timeout_timer = QTimer(self)
        self.download_timeout_timer.setSingleShot(True)
        self.download_timeout_timer.setInterval(Settings().get(SettingsKeys.DownloadTimeout, DownloadTimeout.FiveMinutes.value, int))
        self.download_timeout_timer.timeout.connect(self._on_downloader_timeout_timer_timeout)
        self.download_speed_timer = QTimer(self)
        self.download_speed_timer.setInterval(1_000)
        self.download_speed_timer.timeout.connect(self._on_downloader_speed_timer_timeout)

        self.downloader = QNetworkAccessManager(self)
        self.downloader.finished.connect(self._on_downloader_finished)

        self.installation_proc = QProcess(self)
        self.installation_proc.errorOccurred.connect(self._on_installation_proc_error_occurred)
        self.installation_proc.finished.connect(self._on_installation_proc_finished)

        self.setObjectName('SoftwareProgressRow')
        self.setFixedHeight(36)
        self.setLayout(self._create_layout())
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

    @property
    def is_downloaded(self):
        return self.download_url is not None and self.download_file is not None

    #region Slots
    @Slot(str)
    def _on_software_download_url_resolved(self, url: str):
        if self.cancel_requested or self.operation_finished:
            return

        self.set_status('Download URL resolved')
        self.download_url = url
        self.url_resolved.emit(url)

        if self.software.should_cache_url:
            self.software.cached_url = url

        self._start_download(url)

    @Slot(BaseSoftware.ResolveError)
    def _on_software_download_url_resolve_error_occurred(self):
        if self.cancel_requested or self.operation_finished:
            return

        self._emit_error(self.OperationError.DownloadURLResolveError)

    @Slot()
    def _on_downloader_speed_timer_timeout(self):
        bytes_diff = self.current_bytes - self.last_bytes
        self.current_speed = bytes_diff
        self.last_bytes = self.current_bytes
        self.formatted_speed = self._format_speed(self.current_speed)

    @Slot()
    def _on_downloader_timeout_timer_timeout(self):
        if self.download_reply is None:
            return

        self.download_timed_out = True
        self.download_reply.abort()

    @Slot(int, int)
    def _on_downloader_download_progress(self, current_bytes: int, total_bytes: int):
        if current_bytes > self.current_bytes:
            self._record_download_activity()

        if not self.progress_bar.isVisible():
            self.progress_bar.setVisible(True)

            if total_bytes > 0:
                self.progress_bar.setMaximum(total_bytes)
            else:
                self.progress_bar.setMaximum(0)

        if total_bytes > 0:
            self.progress_bar.setValue(current_bytes)
            status_text = f'Downloading: {self._format_bytes(current_bytes)}/{self._format_bytes(total_bytes)}'
        else:
            status_text = f'Downloading: {self._format_bytes(current_bytes)}'

        if self.formatted_speed != '':
            status_text += f' ({self.formatted_speed})'

        self.set_status(status_text)
        self.current_bytes = current_bytes

    @Slot()
    def _on_downloader_ready_read(self):
        if self.download_reply is None or self.download_save_file is None or self.download_write_failed:
            return

        data = self.download_reply.readAll()
        if data.isEmpty():
            return

        if self.download_save_file.write(data) != data.size():
            self.download_write_failed = True
            self.download_timeout_timer.stop()
            self.download_save_file.cancelWriting()
            self.download_reply.abort()
        else:
            self._record_download_activity()

    @Slot(QNetworkReply)
    def _on_downloader_finished(self, reply: QNetworkReply):
        self.download_timeout_timer.stop()
        self.download_speed_timer.stop()

        error = reply.error()
        if self.download_timed_out:
            self._discard_partial_download()
            self._emit_error(self.OperationError.FileDownloadTimeoutError)
        elif self.cancel_requested:
            self._discard_partial_download()
            self._finish(self.OperationError.Canceled)
        elif self.probing:
            if error == QNetworkReply.NetworkError.NoError:
                self.set_status('<b style="color:green;">OK</b>')
                self._finish(self.OperationError.NoError)
            elif error == QNetworkReply.NetworkError.OperationCanceledError:
                self._emit_error(self.OperationError.Canceled)
            else:
                self._emit_error(self.OperationError.FileDownloadNetworkError)
        elif self.download_write_failed:
            self._discard_partial_download()
            self._emit_error(self.OperationError.FileDownloadIOError)
        elif error == QNetworkReply.NetworkError.NoError:
            # Drain any bytes delivered immediately before the finished signal.
            self._on_downloader_ready_read()
            if self.download_write_failed or self.download_save_file is None:
                self._discard_partial_download()
                self._emit_error(self.OperationError.FileDownloadIOError)
            elif not self.download_save_file.commit():
                self.download_save_file = None
                self._emit_error(self.OperationError.FileDownloadIOError)
            else:
                self.download_save_file = None
                self.download_file = QFile(str(DOWNLOAD_DIR / self.software.download_name))
                self._on_file_written(self.download_file)
        elif error == QNetworkReply.NetworkError.OperationCanceledError:
            self._discard_partial_download()
            self._emit_error(self.OperationError.Canceled)
        else:
            self._discard_partial_download()
            self._emit_error(self.OperationError.FileDownloadNetworkError)

        if self.download_reply is reply:
            self.download_reply = None
        reply.deleteLater()

    @Slot(QFile)
    def _on_file_written(self, file: QFile):
        self.file_downloaded.emit(file)

        if self.skip_installation or self.software.is_archive or not self.download_file.exists():
            self.name.setVisible(True)
            self.progress_bar.setVisible(False)
            self.spinner.stop()
            self.spinner.setVisible(False)

            if self.software.is_archive:
                self.set_status('Archive downloaded')
            else:
                self.set_status('Download complete')

            self._finish(self.OperationError.NoError)
        else:
            self.name.setVisible(True)
            self.progress_bar.setVisible(False)
            self.spinner.stop()
            self.spinner.setVisible(False)
            self.set_status('Waiting to install', True)
            self.installation_requested.emit()

    def _discard_partial_download(self):
        if self.download_save_file is not None:
            self.download_save_file.cancelWriting()
            self.download_save_file = None

    @Slot(QProcess.ProcessError)
    def _on_installation_proc_error_occurred(self):
        if self.cancel_requested:
            self._finish(self.OperationError.Canceled)
        else:
            self._emit_error(self.OperationError.InstallationProcessError)

    @Slot(int, QProcess.ExitStatus)
    def _on_installation_proc_finished(self, exit_code: int, exit_status: QProcess.ExitStatus):
        if self.cancel_requested:
            self._finish(self.OperationError.Canceled)
            return

        succeeded = (
            exit_status == QProcess.ExitStatus.NormalExit and
            exit_code in self.software.successful_install_exit_codes
        )
        if not succeeded:
            self._emit_error(self.OperationError.InstallationProcessError)
            return

        if self.cleanup_postinstall and self.download_file:
            self.download_file.remove()

        self._finish(self.OperationError.NoError)
    #endregion

    #region UI Setup
    def _create_progress_bar(self):
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setVisible(False)
        self.progress_bar.setFixedWidth(100)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setValue(0)

        return self.progress_bar

    def _create_layout(self):
        self.image = QLabel()
        self.image.setFixedSize(18, 18)
        self.image.setScaledContents(True)
        self.image.setPixmap(QPixmap(f':images/software/{self.software.icon}'))
        self.image.setToolTip(self.software.name)

        self.name = QLabel(self.software.name, self)

        self.spinner = Spinner(Spinner.SpinnerStyle.Solid, self)
        self.spinner.setVisible(False)

        self.status = LoadingLabel('', self)

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.image)
        self.layout.addWidget(self.name)
        self.layout.addWidget(self.spinner)
        self.layout.addStretch()
        self.layout.addWidget(self.status)
        self.layout.addWidget(self._create_progress_bar())

        return self.layout
    #endregion

    def set_status(self, status: str, animating: bool = False):
        self.status.set_base_text(status)
        if animating:
            self.status.start_animation()
        else:
            self.status.stop_animation()

    def start_download(self, skip_installation: bool, install_silently: bool, cleanup_postinstall: bool, probe: bool = False):
        self.cancel_requested = False
        self.operation_finished = False
        self.probing = probe
        self.skip_installation = skip_installation
        self.install_silently = install_silently
        self.cleanup_postinstall = cleanup_postinstall

        self.spinner.setVisible(True)
        self.spinner.start()

        if self.software.cached_url:
            self.set_status('Using cached download URL')
            self.download_url = self.software.cached_url
            self._start_download(self.download_url)
        else:
            self.set_status('Resolving download URL', True)
            self.url_resolving.emit()
            self.software.resolve_download_url()

    def cancel(self):
        if self.operation_finished or self.cancel_requested:
            return

        self.cancel_requested = True
        self.download_timed_out = False
        self.download_timeout_timer.stop()

        if self.download_reply:
            self.download_reply.abort()

        for resolver_reply in self.software.findChildren(QNetworkReply):
            resolver_reply.abort()

        self._discard_partial_download()

        if self.installation_proc.state() != QProcess.ProcessState.NotRunning:
            self.installation_proc.kill()
        elif self.download_reply is None:
            # URL resolution has no row-owned reply to abort. Finish immediately;
            # delayed resolver signals are ignored by the guards above.
            self._finish(self.OperationError.Canceled)

        self.set_status('<b style="color:red;">Canceled</b>')
        self.spinner.stop()
        self.spinner.setVisible(False)
        self.progress_bar.setVisible(False)

    def start_installation(self):
        self.spinner.setVisible(True)
        self.spinner.start()

        if self.skip_installation or self.software.is_archive or not self.download_file.exists():
            self._finish(self.OperationError.NoError)
            return

        self.set_status(f'Installing <b>{self.software.download_name}</b>')

        executable = self.download_file.fileName()
        if executable.lower().endswith('.msi'):
            extra_args = ['/qn', '/norestart'] if self.install_silently else []
            self.installation_proc.start('msiexec.exe', ['/i', executable] + extra_args)
        else:
            extra_args = self.software.silent_install_args if self.install_silently else []
            self.installation_proc.start(executable, extra_args)

    def _start_download(self, url: str):
        self.file_downloading.emit(url)
        self.download_timed_out = False

        req = QNetworkRequest(url)
        req.setHeader(QNetworkRequest.KnownHeaders.UserAgentHeader, BROWSER_USER_AGENT)

        if self.probing:
            self.download_reply = self.downloader.head(req)
        else:
            self.download_save_file = QSaveFile(str(DOWNLOAD_DIR / self.software.download_name))
            if not self.download_save_file.open(QIODevice.OpenModeFlag.WriteOnly):
                self.download_save_file = None
                self._emit_error(self.OperationError.FileDownloadIOError)
                return

            self.download_write_failed = False
            self.download_reply = self.downloader.get(req)
            self.download_reply.setReadBufferSize(1024 * 1024)
            self.download_reply.readyRead.connect(self._on_downloader_ready_read)
            self.download_reply.downloadProgress.connect(self._on_downloader_download_progress)

        self.download_timeout_timer.start()
        self.download_speed_timer.start()

    def _record_download_activity(self):
        if (
            self.download_reply is not None and
            not self.download_reply.isFinished() and
            not self.cancel_requested and
            not self.download_timed_out
        ):
            self.download_timeout_timer.start()

    def _emit_error(self, error: OperationError):
        messages = {
            self.OperationError.DownloadURLResolveError: '<b style="color:red;">Failed to resolve download URL</b>',
            self.OperationError.FileDownloadNetworkError: '<b style="color:red;">Download failed</b>',
            self.OperationError.FileDownloadTimeoutError: '<b style="color:red;">Download timed out</b>',
            self.OperationError.FileDownloadIOError: '<b style="color:red;">Failed to write file</b>',
            self.OperationError.InstallationProcessError: '<b style="color:red;">Installation failed</b>',
            self.OperationError.Canceled: '<b style="color:orange;">Canceled</b>',
        }
        self.set_status(messages.get(error, f'<b style="color:red;">{error}</b>'))
        self.spinner.stop()
        self.spinner.setVisible(False)
        self._finish(error)

    def _finish(self, error: OperationError):
        if self.operation_finished:
            return

        self.operation_finished = True
        self.finished.emit(error)

    def _format_bytes(self, size_in_bytes: int):
        for unit in ('', 'K', 'M', 'G', 'T', 'P', 'E', 'Z'):
            if abs(size_in_bytes) < 1024.0:
                return f'{size_in_bytes:3.1f} {unit}B'
            size_in_bytes /= 1024.0
        return f'{size_in_bytes:.1f} YB'

    def _format_speed(self, speed_bps):
        if speed_bps == 0:
            return "0 B/s"

        units = ['B/s', 'KB/s', 'MB/s', 'GB/s']
        speed = float(speed_bps)
        unit_index = 0

        while speed >= 1024.0 and unit_index < len(units) - 1:
            speed /= 1024.0
            unit_index += 1

        return f"{speed:.2f} {units[unit_index]}"
