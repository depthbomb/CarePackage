from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Foobar2000(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'foobar2000'
        self.name = 'foobar2000'
        self.category = SoftwareCategory.Media
        self.download_name = 'foobar2000-x64.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'foobar2000.png'
        self.homepage = 'https://foobar2000.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'foobar2000-x64_v\d+\.\d+\.\d+\.exe')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(f'https://foobar2000.org/files/{match.group(0)}')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.foobar2000.org/download'))
