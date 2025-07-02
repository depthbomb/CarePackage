from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class PlexDesktop(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'plex-desktop'
        self.name = 'Plex Desktop'
        self.download_name = 'Plex-x86_64.exe'
        self.should_cache_url = True
        self.icon = 'plex-desktop.png'
        self.homepage = 'https://plex.tv'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://downloads\.plex\.tv/plex-desktop/\d+\.\d+\.\d+\.\d+-[a-f0-9]{8}/windows/Plex-\d+\.\d+\.\d+\.\d+-[a-f0-9]{8}-x86_64\.exe')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://plex.tv/api/downloads/6.json'))
