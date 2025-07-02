from src.lib.software import BaseSoftware, SoftwareCategory

class GogGalaxy(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'gog-galaxy'
        self.name = 'GOG Galaxy'
        self.category = [SoftwareCategory.Gaming]
        self.download_name = 'GOG_Galaxy_2.0.exe'
        self.icon = 'gog-galaxy.png'
        self.homepage = 'https://gog.com/galaxy'

    def resolve_download_url(self):
        self.url_resolved.emit('https://webinstallers.gog-statics.com/download/GOG_Galaxy_2.0.exe')
