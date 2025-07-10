from src.lib.software import BaseSoftware, SoftwareCategory

class MullvadVPN(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'mullvad-vpn'
        self.name = 'Mullvad VPN'
        self.category = [SoftwareCategory.Security]
        self.download_name = 'Install Mullvad VPN.exe'
        self.icon = 'mullvad-vpn.png'
        self.homepage = 'https://mullvad.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://mullvad.net/en/download/installer/exe/latest')
