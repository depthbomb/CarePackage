from src.lib.software import BaseSoftware, SoftwareCategory

class Bitwarden(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'bitwarden-desktop'
        self.name = 'Bitwarden'
        self.category = [SoftwareCategory.Security]
        self.download_name = 'Bitwarden-Installer.exe'
        self.icon = 'bitwarden.png'
        self.homepage = 'https://bitwarden.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://vault.bitwarden.com/download/?app=desktop&platform=windows&variant=exe')
