from src.lib.software import BaseSoftware, SoftwareCategory

class Spotify(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'spotify'
        self.name = 'Spotify'
        self.category = SoftwareCategory.Media
        self.download_name = 'SpotifySetup.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'spotify.png'
        self.homepage = 'https://spotify.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.scdn.co/SpotifySetup.exe')
