from src.lib.software import BaseSoftware, SoftwareCategory

class InnoSetup(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'inno-setup'
        self.name = 'Inno Setup'
        self.category = [SoftwareCategory.Development]
        self.download_name = 'innosetup.exe'
        self.silent_install_args = ['/VERYSILENT', '/SUPPRESSMSGBOXES', '/NORESTART', '/SP-']
        self.icon = 'inno-setup.png'
        self.homepage = 'https://jrsoftware.org/isinfo.php'

    def resolve_download_url(self):
        self.url_resolved.emit('https://jrsoftware.org/download.php/is.exe?site=1')
