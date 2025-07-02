from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class NvidiaApp(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'nvidia-app'
        self.name = 'NVIDIA App'
        self.category = [SoftwareCategory.Peripheral]
        self.download_name = 'NVIDIA_app.exe'
        self.should_cache_url = True
        self.requires_admin = True
        self.icon = 'nvidia.png'
        self.homepage = 'https://www.nvidia.com/en-us/software/nvidia-app/'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://us.download.nvidia.com/nvapp/client/.*/NVIDIA_app_.*\.exe')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.nvidia.com/en-us/software/nvidia-app/'))
