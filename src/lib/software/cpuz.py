from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class CPUZ(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'cpuz'
        self.name = 'CPU-Z (Classic)'
        self.category = [SoftwareCategory.Utility]
        self.download_name = 'cpu-z.exe'
        self.should_cache_url = True
        self.icon = 'cpuz.png'
        self.homepage = 'https://cpuid.com/softwares/cpu-z.html'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        html = reply.readAll().data().decode()

        version_pattern = compile(r'(\d\.\d+)-en\.exe')
        match = version_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(f'https://download.cpuid.com/cpu-z/cpu-z_{match.group(1)}-en.exe')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest(self.homepage))
