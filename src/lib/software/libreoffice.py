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

        self._initial_url = QUrl('https://libreoffice.org/download/download-libreoffice')

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        if reply.url() == self._initial_url:
            url = reply.url().toString()
            url += 'windows/64-bit/exe/dl'
            self.manager.get(QNetworkRequest(url))
        else:
            pattern = compile(r'href=\'/download/download-libreoffice/\?type=win-x86_64&version=(\d+\.\d+\.\d)+&lang=en-US\'><i class=".*"></i>Windows x86_64 \(Windows 7 or newer required\)')
            html = reply.readAll().data().decode()
            match = pattern.search(html)
            if not match:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            else:
                version = match.group(1)
                self.url_resolved.emit(f'https://mirror.usi.edu/pub/tdf/libreoffice/stable/{version}/win/x86_64/LibreOffice_{version}_Win_x86-64.msi')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest(self._initial_url))
