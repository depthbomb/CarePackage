from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class VeraCrypt(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'veracrypt'
        self.name = 'VeraCrypt'
        self.category = [SoftwareCategory.Security, SoftwareCategory.SystemManagement]
        self.download_name = 'VeraCrypt_Setup_x64.msi'
        self.should_cache_url = True
        self.icon = 'veracrypt.png'
        self.homepage = 'https://veracrypt.io'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://launchpad\.net/veracrypt/trunk/\d\.\d+\.\d+/\+download/VeraCrypt_Setup_x64_\d\.\d+\.\d+\.msi')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://veracrypt.io/en/Downloads.html'))
