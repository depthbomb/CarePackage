from src.lib.software import BaseSoftware

class MullvadVPN(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'Install Mullvad VPN.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://mullvad.net/en/download/installer/exe/latest')
