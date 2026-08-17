from src.lib.software import BaseSoftware

class UbisoftConnect(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'UbisoftConnectInstaller.exe'
        self.silent_install_args = ['/S']

    def resolve_download_url(self):
        self.url_resolved.emit('https://static3.cdn.ubi.com/orbit/launcher_installer/UbisoftConnectInstaller.exe')
