from src.lib.software import BaseSoftware

class Spotify(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'SpotifySetup.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.scdn.co/SpotifySetup.exe')
