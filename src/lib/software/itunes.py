from src.lib.software import BaseSoftware

class ITunes(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'iTunes64Setup.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://www.apple.com/itunes/download/win64')
