from enum import auto, Enum
from typing import cast, Optional
from PySide6.QtGui import QPixmap
from src.widgets.spinner import Spinner
from src.lib.software import BaseSoftware
from src import DOWNLOAD_DIR, BROWSER_USER_AGENT
from src.widgets.loading_label import LoadingLabel
from src.lib.settings import user_settings, DownloadTimeout, UserSettingsKeys
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest, QNetworkAccessManager
from PySide6.QtWidgets import QLabel, QWidget, QSizePolicy, QHBoxLayout, QProgressBar
from PySide6.QtCore import Slot, QFile, Signal, QTimer, QObject, QThread, QProcess, QIODevice

class SoftwareProgressRow(QWidget):
    class OperationError(Enum):
        NoError = auto()
        DownloadURLResolveError = auto()
        FileDownloadTimeoutError = auto()
        FileDownloadNetworkError = auto()
        FileDownloadIOError = auto()
        InstallationProcessError = auto()
        Canceled = auto()

    class ChunkedFileWriter(QObject):
        finished = Signal(QFile)
        error = Signal()
        canceled = Signal()
        progress = Signal(int)

        def __init__(self, file: QFile, reply: QNetworkReply, parent: Optional[QObject] = None):
            super().__init__(parent)
            self.file = file
            self.reply = reply
            self._cancel_requested = False
            self.chunk_size = 1024 * 1024

        def cancel(self):
            self._cancel_requested = True

        @Slot()
        def write_file(self):
            if self._cancel_requested:
                self.canceled.emit()
                return

            if not self.file.open(QIODevice.OpenModeFlag.WriteOnly):
                self.error.emit()
                return

            data = self.reply.readAll().data()
            try:
                total_size = len(data)
                bytes_written = 0

                for i in range(0, total_size, self.chunk_size):
                    if self._cancel_requested:
                        self.file.close()
                        self.file.remove()
                        self.canceled.emit()
                        return

                    chunk = data[i:i + self.chunk_size]
                    written = self.file.write(chunk)

                    if written == -1:
                        self.file.close()
                        self.file.remove()
                        self.error.emit()
                        return

                    bytes_written += written
                    self.progress.emit(bytes_written)

                    QThread.msleep(1)

                self.file.close()
                self.finished.emit(self.file)
            except Exception:
                if self.file.isOpen():
                    self.file.close()
                self.file.remove()
                self.error.emit()
            finally:
                self.reply.deleteLater()

    url_resolving = Signal()
    url_resolved = Signal(str)
    file_downloading = Signal(str)
    file_downloaded = Signal(QFile)
    installation_requested = Signal()
    finished = Signal(OperationError)

    def __init__(self, software: BaseSoftware, parent: Optional[QObject] = None):
        super().__init__(parent)

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

        self.file_writer_thread = cast(Optional[QThread], None)
        self.chunked_writer = cast(Optional[self.ChunkedFileWriter], None)

        self.download_url = cast(Optional[str], None)
        self.download_file = cast(Optional[QFile], None)
        self.download_reply = cast(Optional[QNetworkReply], None)
        self.download_timeout_timer = QTimer(self)
        self.download_timeout_timer.setSingleShot(True)
        self.download_timeout_timer.setInterval(user_settings.value(UserSettingsKeys.DownloadTimeout, DownloadTimeout.FiveMinutes.value, int))
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
        self.set_status('Download URL resolved')
        self.download_url = url
        self.url_resolved.emit(url)

        if self.software.should_cache_url:
            self.software.cached_url = url

        self._start_download(url)

    @Slot(BaseSoftware.ResolveError)
    def _on_software_download_url_resolve_error_occurred(self):
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

        self.download_reply.abort()
        self.download_reply.deleteLater()
        self.download_reply = None

    @Slot(int, int)
    def _on_downloader_download_progress(self, current_bytes: int, total_bytes: int):
        if not self.progress_bar.isVisible() and total_bytes > 0:
            self.progress_bar.setVisible(True)
            self.progress_bar.setMaximum(total_bytes)

        if total_bytes > 0:
            self.progress_bar.setValue(current_bytes)
            status_text = f'Downloading: {self._format_bytes(current_bytes)}/{self._format_bytes(total_bytes)}'
        else:
            status_text = f'Downloading: {self._format_bytes(current_bytes)}'

        if self.formatted_speed != '':
            status_text += f' ({self.formatted_speed})'

        self.set_status(status_text)
        self.current_bytes = current_bytes

    @Slot(QNetworkReply)
    def _on_downloader_finished(self, reply: QNetworkReply):
        error = reply.error()
        if error == QNetworkReply.NetworkError.NoError:
            self.download_timeout_timer.stop()
            self.download_speed_timer.stop()

            self.download_file = QFile(DOWNLOAD_DIR / self.software.download_name)

            self.progress_bar.setMaximum(0)
            if self.current_bytes >= 262_144_000:
                self.set_status('Writing to disk - Don\'t panic if the app freezes!')
            else:
                self.set_status('Writing to disk', True)

            self.file_writer_thread = QThread(self)
            self.chunked_writer = self.ChunkedFileWriter(self.download_file, reply, self)
            self.chunked_writer.moveToThread(self.file_writer_thread)

            self.chunked_writer.finished.connect(self._on_file_written)
            self.chunked_writer.error.connect(lambda: self._emit_error(self.OperationError.FileDownloadIOError))
            self.chunked_writer.canceled.connect(self._on_file_writer_canceled)
            self.chunked_writer.progress.connect(self._on_write_progress)

            self.file_writer_thread.started.connect(self.chunked_writer.write_file)
            self.chunked_writer.finished.connect(self.file_writer_thread.quit)
            self.chunked_writer.finished.connect(self.chunked_writer.deleteLater)
            self.file_writer_thread.finished.connect(self.file_writer_thread.deleteLater)

            self.file_writer_thread.start()
        elif error == QNetworkReply.NetworkError.OperationCanceledError:
            self._emit_error(self.OperationError.Canceled)
        else:
            self._emit_error(self.OperationError.FileDownloadNetworkError)

    @Slot(int)
    def _on_write_progress(self, bytes_written: int):
        self.set_status(f'Writing file to disk ({self._format_bytes(bytes_written)})')

    @Slot()
    def _on_file_writer_canceled(self):
        self.set_status('<b style="color:red;">Write canceled</b>')
        self.finished.emit(self.OperationError.FileDownloadIOError)

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

            self.finished.emit(self.OperationError.NoError)
        else:
            self.name.setVisible(True)
            self.progress_bar.setVisible(False)
            self.spinner.stop()
            self.spinner.setVisible(False)
            self.set_status('Waiting to install', True)
            self.installation_requested.emit()

    @Slot(QProcess.ProcessError)
    def _on_installation_proc_error_occurred(self):
        self._emit_error(self.OperationError.InstallationProcessError)

    @Slot(int, QProcess.ExitStatus)
    def _on_installation_proc_finished(self):
        if self.cleanup_postinstall and self.download_file:
            self.download_file.remove()

        self.finished.emit(self.OperationError.NoError)
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

    def start_download(self, skip_installation: bool, install_silently: bool, cleanup_postinstall: bool):
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
        if self.download_reply:
            self.download_reply.abort()

        if self.chunked_writer is not None:
            self.chunked_writer.cancel()

        self.set_status('<b style="color:red;">Canceled</b>')
        self.spinner.stop()
        self.spinner.setVisible(False)
        self.progress_bar.setVisible(False)

    def start_installation(self):
        self.spinner.setVisible(True)
        self.spinner.start()

        if self.skip_installation or self.software.is_archive or not self.download_file.exists():
            self.finished.emit(self.OperationError.NoError)
            return

        extra_args = []
        if self.install_silently:
            extra_args.extend([
                '--silent', '--no-interaction', '--no-input', '--no-user-input',
                '--quiet', '--passive', '/quiet', '/passive', '/silent', '/q', '/S', '/s'
            ])

        self.set_status(f'Installing <b>{self.software.download_name}</b>')

        executable = self.download_file.fileName()
        if executable.endswith('.msi'):
            self.installation_proc.start('cmd.exe', ['/c', executable] + extra_args)
        else:
            self.installation_proc.start(executable, extra_args)

    def _start_download(self, url: str):
        self.file_downloading.emit(url)

        req = QNetworkRequest(url)
        req.setHeader(QNetworkRequest.KnownHeaders.UserAgentHeader, BROWSER_USER_AGENT)

        self.download_reply = self.downloader.get(req)
        self.download_reply.downloadProgress.connect(self._on_downloader_download_progress)

        self.download_timeout_timer.start()
        self.download_speed_timer.start()

    def _emit_error(self, error: OperationError):
        messages = {
            self.OperationError.DownloadURLResolveError: '<b style="color:red;">Failed to resolve download URL</b>',
            self.OperationError.FileDownloadNetworkError: '<b style="color:red;">Download failed</b>',
            self.OperationError.FileDownloadTimeoutError: '<b style="color:red;">Download timed out</b>',
            self.OperationError.FileDownloadIOError: '<b style="color:red;">Failed to write file</b>',
            self.OperationError.InstallationProcessError: '<b style="color:red;">Failed to start installation</b>',
            self.OperationError.Canceled: '<b style="color:orange;">Canceled</b>',
        }
        self.set_status(messages.get(error, f'<b style="color:red;">{error}</b>'))
        self.spinner.stop()
        self.spinner.setVisible(False)
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
