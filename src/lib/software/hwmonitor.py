from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class HWMonitor(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'hwmonitor'
        self.name = 'HWMonitor'
        self.category = SoftwareCategory.Utility
        self.download_name = 'hwmonitor.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'hwmonitor.png'
        self.homepage = 'https://cpuid.com/softwares/hwmonitor.html'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        html = reply.readAll().data().decode()

        version_pattern = compile(r'(\d\.\d+)\.exe')
        match = version_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(f'https://download.cpuid.com/hwmonitor/hwmonitor_{match.group(1)}.exe')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest(self.homepage))
