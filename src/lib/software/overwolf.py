from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Overwolf(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'overwolf'
        self.name = 'Overwolf'
        self.category = SoftwareCategory.Gaming
        self.download_name = 'OverwolfSetup.zip'
        self.is_archive = True
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'overwolf.png'
        self.homepage = 'https://overwolf.com'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://setup-overwolf-com\.akamaized\.net/\d+\.\d+\.\d+\.\d+/OverwolfSetup\.zip')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://content.overwolf.com/downloads/setup/latest/regular.html'))
