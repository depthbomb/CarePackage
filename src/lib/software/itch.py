from src.lib.software import BaseSoftware, SoftwareCategory

class Itch(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'itch'
        self.name = 'itch'
        self.category = [SoftwareCategory.Gaming]
        self.download_name = 'itch-setup.exe'
        self.is_archive = False
        self.icon = 'itch.png'
        self.homepage = 'https://itch.io/app'

    def resolve_download_url(self):
        self.url_resolved.emit('https://itch.io/app/download')
