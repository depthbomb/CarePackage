from src.lib.software import BaseSoftware

class Medal(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'MedalSetup.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://install.medal.tv')
