from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Wireshark(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'wireshark'
        self.name = 'Wireshark'
        self.category = [SoftwareCategory.Network, SoftwareCategory.Utility]
        self.download_name = 'Wireshark-x64.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = True
        self.icon = 'wireshark.png'
        self.homepage = 'https://wireshark.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        pattern = compile(r'https://\d+.na.dl.wireshark.org/win64/Wireshark-\d+.\d+.\d+-x64.exe')
        html = reply.readAll().data().decode()
        match = pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest(self.homepage))
