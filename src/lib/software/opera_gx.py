from src.lib.software import BaseSoftware, SoftwareCategory

class OperaGx(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'opera-gx'
        self.name = 'Opera GX'
        self.category = SoftwareCategory.Browser
        self.download_name = 'OperaGXSetup.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'operagx.png'
        self.homepage = 'https://opera.com/gx'

    def resolve_download_url(self):
        self.url_resolved.emit('https://net.geo.opera.com/opera_gx/stable/windows')
