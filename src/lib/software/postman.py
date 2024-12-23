from src.lib.software import BaseSoftware, SoftwareCategory

class Postman(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'postman'
        self.name = 'Postman'
        self.category = SoftwareCategory.Development
        self.download_name = 'Postman-win64-Setup.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'postman.png'
        self.homepage = 'https://postman.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://dl.pstmn.io/download/latest/win64')