from src.lib.software import BaseSoftware

class Opera(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'OperaSetup.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://net.geo.opera.com/opera/stable/windows')
