from re import compile
from PySide6.QtCore import Slot, QUrl
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class LibreOffice(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'libreoffice'
        self.name = 'LibreOffice'
        self.category = [SoftwareCategory.Productivity]
        self.download_name = 'LibreOffice_Win_x86-64.msi'
        self.is_archive = False
        self.should_cache_url = True
        self.icon = 'libreoffice.png'
        self.homepage = 'https://libreoffice.org'

        self._initial_url = QUrl('https://www.libreoffice.org/download/')

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        pattern = compile(r'/stable/(\d+\.\d+\.\d+)/')
        html = reply.readAll().data().decode()
        match = pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            version = match.group(1)
            self.url_resolved.emit(f'https://download.documentfoundation.org/libreoffice/stable/{version}/win/x86_64/LibreOffice_{version}_Win_x86-64.msi')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest(self._initial_url))
