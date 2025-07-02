from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Plexamp(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'plexamp'
        self.name = 'Plexamp'
        self.download_name = 'Plexamp Setup.exe'
        self.should_cache_url = True
        self.icon = 'plexamp.png'
        self.homepage = 'https://plex.tv'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https:\\/\\/plexamp\.plex\.tv\\/plexamp\.plex\.tv\\/desktop\\/Plexamp%20Setup%20\d+\.\d+\.\d+\.exe')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0).replace('\\', ''))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.plex.tv/wp-json/plex/v1/downloads/plexamp'))
