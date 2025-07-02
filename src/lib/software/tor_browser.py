from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class TorBrowser(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'tor-browser'
        self.name = 'Tor Browser'
        self.category = [SoftwareCategory.Browser, SoftwareCategory.Security]
        self.download_name = 'tor-browser-windows-x86_64-portable.exe'
        self.should_cache_url = True
        self.icon = 'tor-browser.png'
        self.homepage = 'https://torproject.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'/dist/torbrowser/\d+\.\d+\.\d+/tor-browser-windows-x86_64-portable-\d+\.\d+\.\d+\.exe')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(f'https://www.torproject.org{match.group(0)}')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.torproject.org/download/'))
