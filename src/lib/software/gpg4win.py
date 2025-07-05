from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Gpg4win(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'gpg4win'
        self.name = 'Gpg4win'
        self.category = [SoftwareCategory.Security]
        self.download_name = 'gpg4win.exe'
        self.should_cache_url = True
        self.icon = 'gpg4win.png'
        self.homepage = 'https://gpg4win.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://files\.gpg4win\.org/gpg4win-\d+\.\d+\.\d+\.exe')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.gpg4win.org/thanks-for-download.html'))
