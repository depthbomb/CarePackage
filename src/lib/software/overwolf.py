from src.lib.software import BaseSoftware, SoftwareCategory

class Overwolf(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'overwolf'
        self.name = 'Overwolf'
        self.category = [SoftwareCategory.Gaming]
        self.download_name = 'OverwolfInstaller.exe'
        self.icon = 'overwolf.png'
        self.homepage = 'https://overwolf.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.overwolf.com/install/Download')
