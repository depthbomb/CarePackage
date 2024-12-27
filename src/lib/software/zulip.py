from src.lib.software import BaseSoftware, SoftwareCategory

class Zulip(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'zulip'
        self.name = 'Zulip'
        self.category = SoftwareCategory.Social
        self.download_name = 'Zulip-Web-Setup.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'zulip.png'
        self.homepage = 'https://zulip.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://zulip.com/apps/download/windows')
