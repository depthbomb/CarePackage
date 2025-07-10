from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class SumatraPDF(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'sumatra-pdf'
        self.name = 'Sumatra PDF'
        self.category = [SoftwareCategory.Utility]
        self.download_name = 'SumatraPDF-64-install.exe'
        self.should_cache_url = True
        self.icon = 'sumatrapdf.png'
        self.homepage = 'https://www.sumatrapdfreader.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        html = reply.readAll().data().decode()

        pattern = compile(r'/dl/rel/\d+\.\d+\.\d+/SumatraPDF-\d+\.\d+\.\d+-64-install\.exe')
        match = pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(f'https://www.sumatrapdfreader.org{match.group(0)}')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.sumatrapdfreader.org/download-free-pdf-viewer'))
