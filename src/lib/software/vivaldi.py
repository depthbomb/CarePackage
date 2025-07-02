from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Vivaldi(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'vivaldi'
        self.name = 'Vivaldi'
        self.category = [SoftwareCategory.Browser]
        self.download_name = 'Vivaldi.x64.exe'
        self.icon = 'vivaldi.png'
        self.homepage = 'https://vivaldi.com'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'class="download-button download-link" href="(https://downloads\.vivaldi\.com/stable/Vivaldi\.\d+\.\d+\.\d+\.\d+\.x64\.exe)"')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(1))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://vivaldi.com/download/'))
