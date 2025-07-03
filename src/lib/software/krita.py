from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Krita(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'krita'
        self.name = 'Krita'
        self.category = [SoftwareCategory.Creative]
        self.download_name = 'krita-x64-setup.exe'
        self.should_cache_url = True
        self.icon = 'krita.png'
        self.homepage = 'https://krita.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://download\.kde\.org/stable/krita/\d+\.\d+\.\d+/krita-x64-\d+\.\d+\.\d+-setup\.exe')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://krita.org/en/download'))
