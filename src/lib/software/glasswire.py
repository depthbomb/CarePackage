from src.lib.software import BaseSoftware

class GlassWire(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'GlassWireSetup.exe'
        self.silent_install_args = ['/S']

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.glasswire.com/GlassWireSetup.exe')
