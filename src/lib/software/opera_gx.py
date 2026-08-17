from src.lib.software import BaseSoftware

class OperaGx(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'OperaGXSetup.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://net.geo.opera.com/opera_gx/stable/windows')
