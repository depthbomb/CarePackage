from src.lib.software import BaseSoftware

class Bitwarden(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'Bitwarden-Installer.exe'
        self.silent_install_args = ['/S']

    def resolve_download_url(self):
        self.url_resolved.emit('https://vault.bitwarden.com/download/?app=desktop&platform=windows&variant=exe')
