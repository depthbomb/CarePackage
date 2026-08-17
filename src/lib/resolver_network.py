from typing import cast, Optional
from collections.abc import Callable
from PySide6.QtCore import Slot, Signal, QObject, QByteArray, QCoreApplication
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest, QNetworkAccessManager

_shared_resolver_manager: Optional[QNetworkAccessManager] = None
_shared_download_manager: Optional[QNetworkAccessManager] = None

def shared_resolver_manager() -> QNetworkAccessManager:
    global _shared_resolver_manager

    if _shared_resolver_manager is None:
        _shared_resolver_manager = QNetworkAccessManager(QCoreApplication.instance())
        _shared_resolver_manager.setTransferTimeout(5_000)

    return _shared_resolver_manager


def shared_download_manager() -> QNetworkAccessManager:
    global _shared_download_manager

    if _shared_download_manager is None:
        _shared_download_manager = QNetworkAccessManager(QCoreApplication.instance())

    return _shared_download_manager


class NetworkSession(QObject):
    finished = Signal(QNetworkReply)

    def __init__(self, manager_factory: Callable[[], QNetworkAccessManager], parent: Optional[QObject] = None):
        super().__init__(parent)
        self._manager_factory = manager_factory
        self._active_replies: set[QNetworkReply] = set()

    def get(self, request: QNetworkRequest) -> QNetworkReply:
        return self._track(self._manager_factory().get(request))

    def post(self, request: QNetworkRequest, data: QByteArray) -> QNetworkReply:
        return self._track(self._manager_factory().post(request, data))

    def abort_all(self):
        for reply in tuple(self._active_replies):
            reply.abort()

    @Slot()
    def _on_reply_finished(self):
        reply = cast(QNetworkReply, self.sender())
        self._active_replies.discard(reply)
        self.finished.emit(reply)

    def _track(self, reply: QNetworkReply) -> QNetworkReply:
        self._active_replies.add(reply)
        reply.finished.connect(self._on_reply_finished)
        return reply


class ResolverNetworkSession(NetworkSession):
    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(shared_resolver_manager, parent)


class DownloadNetworkSession(NetworkSession):
    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(shared_download_manager, parent)
