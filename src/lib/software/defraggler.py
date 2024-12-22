from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Defraggler(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'defraggler'
        self.name = 'Defraggler'
        self.category = SoftwareCategory.Utility
        self.download_name = 'dfsetup.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = True
        self.icon = 'defraggler.png'
        self.homepage = 'https://ccleaner.com/defraggler'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://download\.ccleaner\.com/dfsetup(\d){3,}\.exe')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.ccleaner.com/defraggler/download/standard'))
