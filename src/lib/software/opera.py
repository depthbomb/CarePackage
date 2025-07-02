from src.lib.software import BaseSoftware, SoftwareCategory

class Opera(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'opera'
        self.name = 'Opera'
        self.category = [SoftwareCategory.Browser]
        self.download_name = 'OperaSetup.exe'
        self.icon = 'opera.png'
        self.homepage = 'https://opera.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://net.geo.opera.com/opera/stable/windows')
