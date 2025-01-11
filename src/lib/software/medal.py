from src.lib.software import BaseSoftware, SoftwareCategory

class Medal(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'medal'
        self.name = 'Medal'
        self.category = SoftwareCategory.Gaming
        self.download_name = 'MedalSetup.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'medal.png'
        self.homepage = 'https://medal.tv'

    def resolve_download_url(self):
        self.url_resolved.emit('https://install.medal.tv')
