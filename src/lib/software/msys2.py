from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class MSYS2(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'msys2'
        self.name = 'MSYS2'
        self.category = [SoftwareCategory.Development]
        self.download_name = 'msys2-x84_64.exe'
        self.should_cache_url = True
        self.icon = 'msys2.png'
        self.homepage = 'https://msys2.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://github\.com/msys2/msys2-installer/releases/download/\d{4}-\d{2}-\d{2}/msys2-x86_64-\d{8}\.exe')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.msys2.org/'))
