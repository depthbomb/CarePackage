from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Joplin(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'joplin'
        self.name = 'Joplin'
        self.category = [SoftwareCategory.Productivity]
        self.download_name = 'Joplin-Setup.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.icon = 'joplin.png'
        self.homepage = 'https://joplinapp.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://objects\.joplinusercontent.com/v\d+.\d+.\d+/Joplin-Setup-\d+.\d+.\d+.exe')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://joplinapp.org/download'))
