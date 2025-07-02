from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class RPCS3(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'rpcs3'
        self.name = 'RPCS3'
        self.category = [SoftwareCategory.Emulation, SoftwareCategory.Gaming]
        self.download_name = 'rpcs3-build-win64.7z'
        self.is_archive = True
        self.should_cache_url = True
        self.icon = 'rpcs3.png'
        self.homepage = 'https://rpcs3.net'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        html = reply.readAll().data().decode()

        pattern = compile(r'https://github.com/RPCS3/rpcs3-binaries-win/releases/download/build-[a-fA-F0-9]{40}/rpcs3-v\d+.\d+.\d+-\d+-[a-fA-F0-9]{8}_win64.7z')
        match = pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://rpcs3.net/download'))
