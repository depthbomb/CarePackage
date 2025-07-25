from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class OracleVirtualBox(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'oracle-virtualbox'
        self.name = 'Oracle VirtualBox'
        self.category = [SoftwareCategory.Utility]
        self.download_name = 'VirtualBox-Win.exe'
        self.should_cache_url = True
        self.icon = 'oracle-virtualbox.png'
        self.homepage = 'https://virtualbox.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://download\.virtualbox\.org/virtualbox/\d+\.\d+\.\d+/VirtualBox-\d+\.\d+\.\d+-\d{6,}-Win\.exe')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.virtualbox.org/wiki/Downloads'))
