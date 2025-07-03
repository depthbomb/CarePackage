from src.lib.software import BaseSoftware, SoftwareCategory

class Parsec(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'parsec'
        self.name = 'Parsec'
        self.category = [SoftwareCategory.Gaming]
        self.download_name = 'parsec-windows.exe'
        self.icon = 'parsec.png'
        self.homepage = 'https://parsec.app'

    def resolve_download_url(self):
        self.url_resolved.emit('https://builds.parsec.app/package/parsec-windows.exe')
