from os import fsync
from pathlib import Path
from sys import platform
from threading import Event
from typing import Optional
from enum import auto, Enum
from src import BROWSER_USER_AGENT
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest, QNetworkAccessManager
from PySide6.QtCore import Slot, QFile, QTimer, Signal, QObject, QThread, QIODevice, QSaveFile

if platform == 'win32':
    from ctypes import WinDLL
    from msvcrt import get_osfhandle
    from ctypes.wintypes import BOOL, HANDLE

    _flush_file_buffers = WinDLL('kernel32', use_last_error=True).FlushFileBuffers
    _flush_file_buffers.argtypes = [HANDLE]
    _flush_file_buffers.restype = BOOL

class DownloadTaskError(Enum):
    NoError = auto()
    Timeout = auto()
    Network = auto()
    IO = auto()
    Canceled = auto()

class _DownloadWorker(QObject):
    progress = Signal('qint64', 'qint64')
    committing = Signal()
    finished = Signal(DownloadTaskError, str)

    def __init__(
        self,
        url: str,
        destination: Path,
        inactivity_timeout_ms: int,
        probing: bool,
        cancel_requested: Event,
    ):
        super().__init__()
        self.url = url
        self.destination = destination
        self.inactivity_timeout_ms = inactivity_timeout_ms
        self.probing = probing
        self.cancel_requested = cancel_requested

        self.manager: Optional[QNetworkAccessManager] = None
        self.reply: Optional[QNetworkReply] = None
        self.save_file: Optional[QSaveFile] = None
        self.inactivity_timer: Optional[QTimer] = None
        self.last_progress_bytes = 0
        self.probe_succeeded = False
        self.timed_out = False
        self.write_failed = False
        self.result_emitted = False

    @Slot()
    def start(self):
        if self.cancel_requested.is_set():
            self._emit_result(DownloadTaskError.Canceled)
            return

        self.inactivity_timer = QTimer(self)
        self.inactivity_timer.setSingleShot(True)
        self.inactivity_timer.setInterval(self.inactivity_timeout_ms)
        self.inactivity_timer.timeout.connect(self._on_timeout)

        if not self.probing:
            self.save_file = QSaveFile(str(self.destination))
            if not self.save_file.open(QIODevice.OpenModeFlag.WriteOnly):
                self.save_file = None
                self._emit_result(DownloadTaskError.IO)
                return

        request = QNetworkRequest(self.url)
        request.setHeader(QNetworkRequest.KnownHeaders.UserAgentHeader, BROWSER_USER_AGENT)
        if self.probing:
            request.setRawHeader(b'Range', b'bytes=0-0')

        self.manager = QNetworkAccessManager(self)
        self.reply = self.manager.get(request)
        self.reply.finished.connect(self._on_finished)
        self.reply.downloadProgress.connect(self._on_progress)

        if self.probing:
            self.reply.setReadBufferSize(1)
            self.reply.metaDataChanged.connect(self._on_probe_metadata_changed)
        else:
            self.reply.setReadBufferSize(1024 * 1024)
            self.reply.readyRead.connect(self._on_ready_read)

        self.inactivity_timer.start()

    @Slot()
    def cancel(self):
        self.cancel_requested.set()
        if self.inactivity_timer is not None:
            self.inactivity_timer.stop()
        if self.save_file is not None:
            self.save_file.cancelWriting()
        if self.reply is not None:
            self.reply.abort()

    @Slot('qint64', 'qint64')
    def _on_progress(self, current_bytes: int, total_bytes: int):
        if self.result_emitted or self.cancel_requested.is_set() or self.timed_out:
            return

        if current_bytes > self.last_progress_bytes:
            self.last_progress_bytes = current_bytes
            self._record_activity()

        self.progress.emit(current_bytes, total_bytes)

    @Slot()
    def _on_ready_read(self):
        if (
            self.reply is None or
            self.save_file is None or
            self.write_failed or
            self.cancel_requested.is_set()
        ):
            return

        data = self.reply.readAll()
        if data.isEmpty():
            return

        if self.save_file.write(data) != data.size():
            self.write_failed = True
            self.save_file.cancelWriting()
            self.reply.abort()
        else:
            self._record_activity()

    @Slot()
    def _on_probe_metadata_changed(self):
        if self.reply is None or self.cancel_requested.is_set() or self.timed_out:
            return

        status = self.reply.attribute(QNetworkRequest.Attribute.HttpStatusCodeAttribute)
        if status is not None and 200 <= int(status) < 300:
            self.probe_succeeded = True
            self.reply.abort()

    @Slot()
    def _on_timeout(self):
        if self.reply is None:
            return

        self.timed_out = True
        self.reply.abort()

    @Slot()
    def _on_finished(self):
        if self.reply is None:
            return

        reply = self.reply
        error = reply.error()
        if self.inactivity_timer is not None:
            self.inactivity_timer.stop()

        if self.cancel_requested.is_set():
            self._discard_partial_download()
            result = DownloadTaskError.Canceled
            path = ''
        elif self.timed_out:
            self._discard_partial_download()
            result = DownloadTaskError.Timeout
            path = ''
        elif self.probing:
            if self.probe_succeeded or error == QNetworkReply.NetworkError.NoError:
                result = DownloadTaskError.NoError
            elif error == QNetworkReply.NetworkError.OperationCanceledError:
                result = DownloadTaskError.Canceled
            else:
                result = DownloadTaskError.Network
            path = ''
        elif self.write_failed:
            self._discard_partial_download()
            result = DownloadTaskError.IO
            path = ''
        elif error == QNetworkReply.NetworkError.NoError:
            # Drain bytes that may have arrived immediately before finished().
            self._on_ready_read()
            result, path = self._commit_download()
        elif error == QNetworkReply.NetworkError.OperationCanceledError:
            self._discard_partial_download()
            result = DownloadTaskError.Canceled
            path = ''
        else:
            self._discard_partial_download()
            result = DownloadTaskError.Network
            path = ''

        self.reply = None
        reply.deleteLater()
        self._emit_result(result, path)

    def _commit_download(self) -> tuple[DownloadTaskError, str]:
        if self.write_failed or self.save_file is None:
            self._discard_partial_download()
            return DownloadTaskError.IO, ''

        if self.cancel_requested.is_set():
            self._discard_partial_download()
            return DownloadTaskError.Canceled, ''

        save_file = self.save_file
        self.save_file = None
        self.committing.emit()

        # QSaveFile.commit() synchronizes the native handle before its atomic rename. PySide holds the GIL for that
        # call, which can still pause Python-driven GUI updates even from a QThread. Synchronize explicitly through an
        # OS call that releases the GIL, leaving commit() with only a cheap close and rename.
        if not save_file.flush() or not self._sync_to_disk(save_file):
            save_file.cancelWriting()
            return DownloadTaskError.IO, ''

        if self.cancel_requested.is_set():
            save_file.cancelWriting()
            return DownloadTaskError.Canceled, ''

        if not save_file.commit():
            return DownloadTaskError.IO, ''

        destination = str(self.destination)
        if self.cancel_requested.is_set():
            QFile(destination).remove()
            return DownloadTaskError.Canceled, ''

        return DownloadTaskError.NoError, destination

    @staticmethod
    def _sync_to_disk(save_file: QSaveFile) -> bool:
        handle = save_file.handle()
        if handle == -1:
            return False

        if platform == 'win32':
            try:
                native_handle = get_osfhandle(handle)
            except OSError:
                return False
            return bool(_flush_file_buffers(HANDLE(native_handle)))

        try:
            fsync(handle)
            return True
        except OSError:
            return False

    def _discard_partial_download(self):
        if self.save_file is not None:
            self.save_file.cancelWriting()
            self.save_file = None

    def _record_activity(self):
        if (
            self.inactivity_timer is not None and
            self.reply is not None and
            not self.reply.isFinished() and
            not self.cancel_requested.is_set() and
            not self.timed_out
        ):
            self.inactivity_timer.start()

    def _emit_result(self, result: DownloadTaskError, path: str = ''):
        if self.result_emitted:
            return

        self.result_emitted = True
        if self.inactivity_timer is not None:
            self.inactivity_timer.stop()
        self.finished.emit(result, path)

class DownloadTask(QObject):
    progress = Signal('qint64', 'qint64')
    committing = Signal()
    completed = Signal(str)
    failed = Signal(DownloadTaskError)
    _cancel_worker = Signal()

    def __init__(
        self,
        url: str,
        destination: Path,
        inactivity_timeout_ms: int,
        probing: bool = False,
        parent: Optional[QObject] = None,
    ):
        super().__init__(parent)
        self._cancel_requested = Event()
        self._result: Optional[tuple[DownloadTaskError, str]] = None
        self._started = False

        self._thread = QThread(self)
        self._worker = _DownloadWorker(
            url,
            destination,
            inactivity_timeout_ms,
            probing,
            self._cancel_requested,
        )
        self._worker.moveToThread(self._thread)

        self._thread.started.connect(self._worker.start)
        self._worker.progress.connect(self.progress)
        self._worker.committing.connect(self.committing)
        self._worker.finished.connect(self._store_result)
        self._worker.finished.connect(self._worker.deleteLater)
        self._worker.finished.connect(self._thread.quit)
        self._thread.finished.connect(self._on_thread_finished)
        self._thread.finished.connect(self._thread.deleteLater)
        self._cancel_worker.connect(self._worker.cancel)

    def start(self):
        if self._started:
            return

        self._started = True
        self._thread.start()

    def cancel(self):
        if not self._started or self._result is not None:
            return

        # The event lets the worker observe cancellation even while commit() is blocking its event loop. The signal
        # handles the interruptible phases.
        self._cancel_requested.set()
        self._cancel_worker.emit()

    @Slot(DownloadTaskError, str)
    def _store_result(self, result: DownloadTaskError, path: str):
        self._result = (result, path)

    @Slot()
    def _on_thread_finished(self):
        if self._result is None:
            # A worker thread should only stop through its terminal signal.
            self.failed.emit(DownloadTaskError.IO)
            return

        result, path = self._result
        self._worker = None
        self._thread = None

        if result == DownloadTaskError.NoError:
            self.completed.emit(path)
        else:
            self.failed.emit(result)
