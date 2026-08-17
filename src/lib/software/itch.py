from src.lib.software import BaseSoftware

class Itch(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'itch-setup.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://itch.io/app/download')
