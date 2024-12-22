from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class QtOss(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'qt-oss'
        self.name = 'Qt'
        self.category = SoftwareCategory.Development
        self.download_name = 'qt-online-installer-windows-x64.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'qt.png'
        self.homepage = 'https://www.qt.io/download-open-source'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'id="download-windows_x64" href="(.*)"')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(1))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.qt.io/download-qt-installer-oss'))
