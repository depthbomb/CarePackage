from src.lib.software import BaseSoftware, SoftwareCategory

class ITunes(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'itunes'
        self.name = 'iTunes'
        self.category = [SoftwareCategory.Audio, SoftwareCategory.Media]
        self.download_name = 'iTunes64Setup.exe'
        self.icon = 'itunes.png'
        self.homepage = 'https://apple.com/itunes'

    def resolve_download_url(self):
        self.url_resolved.emit('https://www.apple.com/itunes/download/win64')
