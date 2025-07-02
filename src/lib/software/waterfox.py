from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Waterfox(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'waterfox'
        self.name = 'Waterfox'
        self.category = [SoftwareCategory.Browser]
        self.download_name = 'Waterfox Setup.exe'
        self.should_cache_url = True
        self.icon = 'waterfox.png'
        self.homepage = 'https://waterfox.net'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://cdn\d+\.waterfox\.net/waterfox/releases/\d+\.\d+\.\d+/WINNT_x86_64/Waterfox%20Setup%20.*\.exe')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.waterfox.net/download/'))
