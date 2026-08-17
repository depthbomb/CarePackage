from src.lib.software import BaseSoftware

class Steam(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'SteamSetup.exe'
        self.silent_install_args = ['/S']

    def resolve_download_url(self):
        self.url_resolved.emit('https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe')
