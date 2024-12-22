from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class ObsStudio(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'obs-studio'
        self.name = 'OBS Studio'
        self.category = SoftwareCategory.Media
        self.download_name = 'OBS-Studio-Windows-Installer.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = True
        self.icon = 'obs-studio.png'
        self.homepage = 'https://obsproject.com'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://cdn-fastly\.obsproject\.com/downloads/OBS-Studio-\d+.\d+.\d+-Windows-Installer\.exe')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://obsproject.com/download'))
