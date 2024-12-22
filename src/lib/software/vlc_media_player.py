from re import compile
from PySide6.QtCore import Slot, QUrl
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class VlcMediaPlayer(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'vlc-media-player'
        self.name = 'VLC Media Player'
        self.category = SoftwareCategory.Media
        self.download_name = 'vlc-win64.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = True
        self.icon = 'vlc-media-player.png'
        self.homepage = 'https://videolan.org'

        self._initial_url = QUrl('https://www.videolan.org/')

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        html = reply.readAll().data().decode()

        if reply.url() == self._initial_url:
            download_page_pattern = compile(r'//get\.videolan\.org/vlc/\d+\.\d+\.\d+/win64/vlc-\d+\.\d+\.\d+-win64\.exe')
            match = download_page_pattern.search(html)
            if not match:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            else:
                req = QNetworkRequest(f'https:{match.group(0)}')
                self.manager.get(req)
        else:
            download_url_pattern = compile(r'URL=\'(.*)\'')
            match = download_url_pattern.search(html)
            if not match:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            else:
                self.url_resolved.emit(match.group(1))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest(self._initial_url))
