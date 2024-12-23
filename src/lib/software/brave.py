from src.lib.software import BaseSoftware, SoftwareCategory

class Brave(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'brave-browser'
        self.name = 'Brave'
        self.category = SoftwareCategory.Browser
        self.download_name = 'BraveBrowserSetup.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'brave-browser.png'
        self.homepage = 'https://brave.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://laptop-updates.brave.com/download/desktop/release/BRV010?bitness=64')
