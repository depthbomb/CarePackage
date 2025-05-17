from typing import Optional
from packaging.version import Version
from src import USER_AGENT, APP_VERSION_STRING
from PySide6.QtCore import Slot, Signal, QTimer, QObject, QJsonDocument
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest, QNetworkAccessManager

class UpdateChecker(QObject):
    update_available = Signal(str)

    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)

        self.manager = QNetworkAccessManager(self)
        self.manager.finished.connect(self._on_manager_finished)

        self.update_timer = QTimer(self)
        self.update_timer.setInterval(1_000 * 90)
        self.update_timer.timeout.connect(self._on_update_timer_timeout)

    #region Slots
    @Slot()
    def _on_update_timer_timeout(self):
        self._check_for_updates()

    @Slot(QNetworkReply)
    def _on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        if reply.error() != QNetworkReply.NetworkError.NoError:
            return

        data = reply.readAll()
        json = QJsonDocument.fromJson(data).array()
        release = None
        for i in range(json.size()):
            item = json.at(i).toObject()
            if not bool(item['prerelease']):
                release = item
                break

        if not release:
            return

        release_url = str(release['html_url'])
        latest_tag = str(release['tag_name'])

        current_version = Version(APP_VERSION_STRING)
        release_version = Version(latest_tag)
        if release_version > current_version:
            self.update_available.emit(release_url)
            self.update_timer.stop()
    #endregion

    def start_checking(self):
        self.update_timer.start()
        self._check_for_updates()

    def _check_for_updates(self):
        req = QNetworkRequest('https://api.github.com/repos/depthbomb/carepackage/releases')
        req.setHeader(QNetworkRequest.KnownHeaders.UserAgentHeader, USER_AGENT)

        self.manager.get(req)
