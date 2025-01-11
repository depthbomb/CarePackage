from src.lib.software import BaseSoftware, SoftwareCategory

class TeraCopy(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'teracopy'
        self.name = 'TeraCopy'
        self.category = SoftwareCategory.Utility
        self.download_name = 'teracopy.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'teracopy.png'
        self.homepage = 'https://codesector.com/teracopy'

    def resolve_download_url(self):
        self.url_resolved.emit('https://www.codesector.com/files/teracopy.exe')
