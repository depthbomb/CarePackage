from src.lib.software import BaseSoftware

class GogGalaxy(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'GOG_Galaxy_2.0.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://webinstallers.gog-statics.com/download/GOG_Galaxy_2.0.exe')
