from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Gimp(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'gimp'
        self.name = 'GIMP'
        self.category = [SoftwareCategory.Creative]
        self.download_name = 'GimpSetup.exe'
        self.should_cache_url = True
        self.icon = 'gimp.png'
        self.homepage = 'https://gimp.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'//download\.gimp\.org/gimp/v\d+\.\d+/windows/gimp-\d+\.\d+\.\d+-setup(-\d+)?\.exe')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(f'https:{match.group(0)}')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.gimp.org/downloads/'))
