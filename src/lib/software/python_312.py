from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Python312(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'python-312'
        self.name = 'Python 3.12.x'
        self.category = SoftwareCategory.Development
        self.download_name = 'python3.12.x-amd64.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'python.png'
        self.homepage = 'https://python.org'

        self._current_ver = 30

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        status_code =  int(reply.attribute(QNetworkRequest.Attribute.HttpStatusCodeAttribute))
        if status_code == 404:
            if self._current_ver <= 0:
                self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)
            else:
                self._current_ver -= 1
                self._try_current_ver()
        else:
            self.url_resolved.emit(reply.url().toString())

    def resolve_download_url(self):
        self._try_current_ver()

    def _try_current_ver(self):
        url = f'https://www.python.org/ftp/python/3.12.{self._current_ver}/python-3.12.{self._current_ver}-amd64.exe'
        req = QNetworkRequest(url)

        self.manager.head(req)
