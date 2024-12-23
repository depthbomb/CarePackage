from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Winrar(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'winrar'
        self.name = 'WinRAR'
        self.category = SoftwareCategory.Utility
        self.download_name = 'WinRAR.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'winrar.png'
        self.homepage = 'https://www.win-rar.com'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'"(/fileadmin/winrar-versions/downloader/WinRAR-\d{2,}\.exe)"')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(f'https://www.win-rar.com{match.group(1)}')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.win-rar.com/download.html?&L=0'))
