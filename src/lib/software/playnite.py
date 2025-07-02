from src.lib.software import BaseSoftware, SoftwareCategory

class Playnite(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'playnite'
        self.name = 'Playnite'
        self.category = [SoftwareCategory.Gaming]
        self.download_name = 'PlayniteInstaller.exe'
        self.icon = 'playnite.png'
        self.homepage = 'https://playnite.link'

    def resolve_download_url(self):
        self.url_resolved.emit('https://playnite.link/download/PlayniteInstaller.exe')
