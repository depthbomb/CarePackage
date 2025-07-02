from re import compile
from PySide6.QtCore import Slot, QUrl
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class WinScp(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'winscp'
        self.name = 'WinSCP'
        self.category = [SoftwareCategory.Network, SoftwareCategory.Utility]
        self.download_name = 'WinSCP-Setup.exe'
        self.icon = 'winscp.png'
        self.homepage = 'https://winscp.net'

        self._initial_url = QUrl('https://winscp.net/eng/download.php')

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        html = reply.readAll().data().decode()

        if reply.url() == self._initial_url:
            download_page_pattern = compile(r'/download/WinSCP-.*-Setup\.exe/download')
            match = download_page_pattern.search(html)
            if not match:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            else:
                req = QNetworkRequest(f'https://winscp.net{match.group(0)}')
                self.manager.get(req)
        else:
            download_url_pattern = compile(r'href="(https://cdn\.winscp\.net/files/WinSCP-.*-Setup\.exe\?secure=.*,\d{10,})"')
            match = download_url_pattern.search(html)
            if not match:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            else:
                self.url_resolved.emit(match.group(1))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest(self._initial_url))
