from re import compile
from enum import auto, Enum
from typing import cast, Optional
from src import BROWSER_USER_AGENT
from PySide6.QtCore import Slot, Signal, QObject
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest, QNetworkAccessManager

class GithubReleaseScraper(QObject):
    class ScraperError(Enum):
        RequestError = auto()

    releases_scraped = Signal(list)
    error_occurred = Signal(ScraperError)

    def __init__(self, owner: str, repo: str, parent: Optional[QObject] = None):
        super().__init__(parent)

        self._owner = owner
        self._repo = repo
        self._tag = cast(Optional[str], None)

        self._manager = QNetworkAccessManager(self)
        self._manager.finished.connect(self._on_manager_finished)
        self._release_href_pattern = compile(r'href="(.*)" rel="nofollow"')

    #region Slots
    @Slot(QNetworkReply)
    def _on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()

        url = reply.url()
        path = url.path()
        code = int(reply.attribute(QNetworkRequest.Attribute.HttpStatusCodeAttribute))

        if 'releases/tag' in path:
            if code > 299:
                self.error_occurred.emit(self.ScraperError.RequestError)
                return

            self._tag = path.split('/')[-1]
            req = QNetworkRequest(f'https://github.com/{self._owner}/{self._repo}/releases/expanded_assets/{self._tag}')
            req.setHeader(QNetworkRequest.KnownHeaders.UserAgentHeader, BROWSER_USER_AGENT)
            self._manager.get(req)
        else:
            if code == 404:
                # Some repositories have their assets located at {owner}/{repo}/releases/expanded_assets/release/{tag}
                # instead of the typical {owner}/{repo}/releases/expanded_assets/{tag} so just make a request to the
                # other URL.
                req = QNetworkRequest(f'https://github.com/{self._owner}/{self._repo}/releases/expanded_assets/release/{self._tag}')
                req.setHeader(QNetworkRequest.KnownHeaders.UserAgentHeader, BROWSER_USER_AGENT)
                self._manager.get(req)
            elif code < 300:
                html = reply.readAll().data().decode()
                matches = self._release_href_pattern.findall(html)
                self.releases_scraped.emit([f'https://github.com{p}' for p in matches])
            else:
                self.error_occurred.emit(self.ScraperError.RequestError)
    #endregion

    def get_repo_releases(self):
        req = QNetworkRequest(f'https://github.com/{self._owner}/{self._repo}/releases/latest')
        req.setHeader(QNetworkRequest.KnownHeaders.UserAgentHeader, BROWSER_USER_AGENT)

        self._manager.get(req)
