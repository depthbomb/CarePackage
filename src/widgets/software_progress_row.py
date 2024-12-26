from enum import auto, Enum
from typing import cast, Optional
from src.widgets.spinner import Spinner
from src.lib.software import BaseSoftware
from PySide6.QtGui import QPixmap, QPalette
from src.lib.colors import get_accent_color
from src import DOWNLOAD_DIR, BROWSER_USER_AGENT
from winrt.windows.ui.viewmanagement import UIColorType
from src.lib.settings import user_settings, DownloadTimeout, UserSettingsKeys
from PySide6.QtCore import Qt, Slot, QFile, Signal, QTimer, QProcess, QIODevice
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest, QNetworkAccessManager
from PySide6.QtWidgets import QLabel, QWidget, QSizePolicy, QHBoxLayout, QProgressBar

class SoftwareProgressRow(QWidget):
    class OperationError(Enum):
        NoError = auto()
        DownloadURLResolveError = auto()
        FileDownloadTimeoutError = auto()
        FileDownloadNetworkError = auto()
        FileDownloadIOError = auto()
        InstallationProcessError = auto()

    url_resolving = Signal()
    url_resolved = Signal(str)
    file_downloading = Signal(str)
    file_downloaded = Signal(QFile)
    finished = Signal(OperationError)

    def __init__(self, software: BaseSoftware, parent: Optional[QWidget] = None):
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

        self.download_url = cast(Optional[str], None)
        self.download_file = cast(Optional[QFile], None)
        self.download_reply  = cast(Optional[QNetworkReply], None)
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
        self.status.setText('Download URL resolved')

        self.download_url = url
        self.url_resolved.emit(url)

        if self.software.should_cache_url:
            self.software.cached_url = url

        self._start_download(url)

    @Slot(BaseSoftware.ResolveError)
    def _on_software_download_url_resolve_error_occurred(self, error: BaseSoftware.ResolveError):
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
            self.name.setVisible(False)
            self.progress_bar.setVisible(True)
            self.progress_bar.setMaximum(total_bytes)

        if total_bytes > 0:
            self.progress_bar.setValue(current_bytes)
            status_text = f'Downloading: {self._format_bytes(current_bytes)}/{self._format_bytes(total_bytes)}'
        else:
            status_text = f'Downloading: {self._format_bytes(current_bytes)}'

        if self.formatted_speed != '':
            status_text += f' ({self.formatted_speed})'

        self.status.setText(status_text)

        self.current_bytes = current_bytes

    @Slot(QNetworkReply)
    def _on_downloader_finished(self, reply: QNetworkReply):
        error = reply.error()
        if error == QNetworkReply.NetworkError.NoError:
            self.download_timeout_timer.stop()
            self.download_timeout_timer.deleteLater()

            self.download_speed_timer.stop()
            self.download_speed_timer.deleteLater()

            self.download_file = QFile(DOWNLOAD_DIR / self.software.download_name)
            if self.download_file.open(QIODevice.OpenModeFlag.WriteOnly):
                self.download_file.write(reply.readAll())
                self.download_file.close()

                self.status.setText('Download complete')

                self.file_downloaded.emit(self.download_file)

                self.start_installation()
            else:
                self._emit_error(self.OperationError.FileDownloadIOError)
        elif error == QNetworkReply.NetworkError.OperationCanceledError:
            self._emit_error(self.OperationError.FileDownloadTimeoutError)
        else:
            self._emit_error(self.OperationError.FileDownloadNetworkError)

    @Slot(QProcess.ProcessError)
    def _on_installation_proc_error_occurred(self, error: QProcess.ProcessError):
        self._emit_error(self.OperationError.InstallationProcessError)

    @Slot(int, QProcess.ExitStatus)
    def _on_installation_proc_finished(self, exit_code: int, exit_status: QProcess.ExitStatus):
        if self.cleanup_postinstall:
            self.download_file.remove()

        self.finished.emit(self.OperationError.NoError)
    #endregion

    #region UI Setup
    def _create_progress_bar(self):
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setVisible(False)
        self.progress_bar.setFixedWidth(100)
        self.progress_bar.setValue(0)
        palette = self.progress_bar.palette()
        palette.setColor(QPalette.ColorRole.Highlight, get_accent_color(UIColorType.ACCENT))
        self.progress_bar.setPalette(palette)

        return self.progress_bar

    def _create_layout(self):
        self.image = QLabel()
        self.image.setFixedSize(16, 16)
        self.image.setScaledContents(True)
        self.image.setPixmap(QPixmap(f':images/software/{self.software.icon}'))
        self.image.setToolTip(self.software.name)

        self.name = QLabel(self.software.name, self)
        self.name.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.spinner = Spinner(Spinner.SpinnerStyle.Dots, self)
        self.spinner.setVisible(False)

        self.status = QLabel(self)

        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.image)
        self.layout.addWidget(self.name)
        self.layout.addWidget(self._create_progress_bar())
        self.layout.addStretch()
        self.layout.addWidget(self.spinner)
        self.layout.addWidget(self.status)

        return self.layout
    #endregion

    def set_status(self, status: str):
        self.status.setText(status)

    def start_download(self, skip_installation: bool, install_silently: bool, cleanup_postinstall: bool):
        self.skip_installation = skip_installation
        self.install_silently = install_silently
        self.cleanup_postinstall = cleanup_postinstall

        self.spinner.setVisible(True)
        self.spinner.start()

        if self.software.cached_url:
            self.status.setText('Using cached download URL')
            self.download_url = self.software.cached_url
            self._start_download(self.download_url)
        else:
            self.status.setText('Resolving download URL...')
            self.url_resolving.emit()
            self.software.resolve_download_url()

    def start_installation(self):
        self.progress_bar.setVisible(False)

        if self.skip_installation or self.software.is_archive or not self.download_file.exists():
            self.finished.emit(self.OperationError.NoError)
            return

        extra_args = []
        if self.install_silently:
            extra_args.append('--silent')
            extra_args.append('--no-interaction')
            extra_args.append('--no-input')
            extra_args.append('--no-user-input')
            extra_args.append('--quiet')
            extra_args.append('--passive')
            extra_args.append('/quiet')
            extra_args.append('/passive')
            extra_args.append('/silent')
            extra_args.append('/q')
            extra_args.append('/S')
            extra_args.append('/s')

        executable = self.download_file.fileName()
        if executable.endswith('.msi'):
            # MSI executables cannot be run via `QProcess.start()` for some reason
            self.installation_proc.start('cmd.exe', ['/c', executable] + extra_args)
        else:
            self.installation_proc.start(executable, extra_args)

        self.status.setText(f'Waiting for <b>{self.software.download_name}</b> to exit...')

    def _start_download(self, url: str):
        self.file_downloading.emit(url)

        req = QNetworkRequest(url)
        req.setHeader(QNetworkRequest.KnownHeaders.UserAgentHeader, BROWSER_USER_AGENT)

        self.download_reply = self.downloader.get(req)
        self.download_reply.downloadProgress.connect(self._on_downloader_download_progress)

        self.download_timeout_timer.start()
        self.download_speed_timer.start()

    def _emit_error(self, error: OperationError):
        match error:
            case self.OperationError.DownloadURLResolveError:
                self.status.setText('<b style="color:red;">Failed to resolve download URL</b>')
            case self.OperationError.FileDownloadNetworkError:
                self.status.setText('<b style="color:red;">Download failed</b>')
            case self.OperationError.FileDownloadTimeoutError:
                self.status.setText('<b style="color:red;">Download timed out</b>')
            case self.OperationError.FileDownloadIOError:
                self.status.setText('<b style="color:red;">Failed to write file</b>')
            case self.OperationError.InstallationProcessError:
                self.status.setText('<b style="color:red;">Failed to start installation</b>')
            case _:
                self.status.setText(f'<b style="color:red;">{error}</b>')

        self.spinner.stop()
        self.spinner.setVisible(False)
        self.finished.emit(error)

    def _format_bytes(self, size_in_bytes: int):
        for unit in ('', 'K', 'M', 'G', 'T', 'P', 'E', 'Z'):
            if abs(size_in_bytes) < 1024.0:
                return f'{size_in_bytes:3.1f} {unit}B'

            size_in_bytes /= 1024.0

        return f'{size_in_bytes:.1f} Y{size_in_bytes}'

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
