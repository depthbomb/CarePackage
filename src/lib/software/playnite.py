from src.lib.software import BaseSoftware

class Playnite(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'PlayniteInstaller.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://playnite.link/download/PlayniteInstaller.exe')
