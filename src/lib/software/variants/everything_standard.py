from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class EverythingStandard(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'everything-standard'
        self.name = 'Everything'
        self.download_name = 'Everything-x64-Setup.exe'
        self.should_cache_url = True
        self.icon = 'everything.png'
        self.homepage = 'https://voidtools.com'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'/Everything-\d\.\d+\.\d+\.\d+\.x64-Setup\.exe')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(f'https://www.voidtools.com{match.group(0)}')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.voidtools.com/'))
