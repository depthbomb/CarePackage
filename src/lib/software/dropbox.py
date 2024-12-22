from src.lib.software import BaseSoftware, SoftwareCategory

class Dropbox(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'dropbox'
        self.name = 'Dropbox'
        self.category = SoftwareCategory.Utility
        self.download_name = 'DropoboxInstaller.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'dropbox.png'
        self.homepage = 'https://dropbox.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://www.dropbox.com/download?os=win&plat=win')
