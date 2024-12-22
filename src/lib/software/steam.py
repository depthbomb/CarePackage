from src.lib.software import BaseSoftware, SoftwareCategory

class Steam(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'steam'
        self.name = 'Steam'
        self.category = SoftwareCategory.Gaming
        self.download_name = 'SteamSetup.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = True
        self.icon = 'steam.png'
        self.homepage = 'https://store.steampowered.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe')
