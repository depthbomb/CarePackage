from re import compile
from typing import cast, Optional
from src import BROWSER_USER_AGENT
from src.lib.software import BaseSoftware
from PySide6.QtCore import Slot, Signal, QObject
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest, QNetworkAccessManager

class GithubReleaseScraper(QObject):
    releases_scraped = Signal(list)

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
        parent = cast(BaseSoftware, self.parent())

        reply.deleteLater()

        url = reply.url()
        path = url.path()
        status_code_attr = reply.attribute(QNetworkRequest.Attribute.HttpStatusCodeAttribute)
        code = int(status_code_attr) if status_code_attr else 999

        if 'releases/tag' in path:
            if code > 299:
                parent.url_resolve_error.emit(parent.ResolveError.GitHubRequestError)
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
                parent.url_resolve_error.emit(parent.ResolveError.GitHubRequestError)
    #endregion

    def get_repo_releases(self):
        req = QNetworkRequest(f'https://github.com/{self._owner}/{self._repo}/releases/latest')
        req.setHeader(QNetworkRequest.KnownHeaders.UserAgentHeader, BROWSER_USER_AGENT)

        self._manager.get(req)
