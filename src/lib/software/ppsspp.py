from re import compile
from PySide6.QtCore import QUrl, Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Ppsspp(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'ppsspp'
        self.name = 'PPSSPP'
        self.category = [SoftwareCategory.Emulation, SoftwareCategory.Gaming]
        self.download_name = 'PPSSPPSetup.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.icon = 'ppsspp.png'
        self.homepage = 'https://ppsspp.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        html = reply.readAll().data().decode()

        pattern = compile(r'https://www\.ppsspp\.org/files/\d+_\d+_\d+/PPSSPPSetup.exe')
        match = pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://ppsspp.org/download/'))
