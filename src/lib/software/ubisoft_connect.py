from src.lib.software import BaseSoftware, SoftwareCategory

class UbisoftConnect(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'ubisoft-connect'
        self.name = 'Ubisoft Connect'
        self.category = [SoftwareCategory.Gaming]
        self.download_name = 'UbisoftConnectInstaller.exe'
        self.requires_admin = True
        self.icon = 'ubisoft-connect.png'
        self.homepage = 'https://ubisoft.com/en-us/ubisoft-connect'

    def resolve_download_url(self):
        self.url_resolved.emit('https://static3.cdn.ubi.com/orbit/launcher_installer/UbisoftConnectInstaller.exe')
