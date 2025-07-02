from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class ElgatoStreamDeck(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'elgato-stream-deck'
        self.name = 'Elgato Stream Deck'
        self.category = [SoftwareCategory.Peripheral]
        self.download_name = 'Stream_Deck.msi'
        self.should_cache_url = True
        self.icon = 'elgato-stream-deck.png'
        self.homepage = 'https://help.elgato.com/hc/en-us/sections/5162671529357-Elgato-Stream-Deck-Software-Release-Notes'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://edge\.elgato\.com/egc/windows/sd/Stream_Deck_\d+\.\d+\.\d+\.\d+\.msi')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.elgato.com/us/en/s/downloads'))
