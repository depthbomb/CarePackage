from src.lib.software import BaseSoftware, SoftwareCategory

class Composer(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'composer'
        self.name = 'Composer'
        self.category = [SoftwareCategory.Development]
        self.download_name = 'Composer-Setup.exe'
        self.icon = 'generic-3.png'
        self.homepage = 'https://getcomposer.org'

    def resolve_download_url(self):
        self.url_resolved.emit('https://getcomposer.org/Composer-Setup.exe')
