from src.lib.software import BaseSoftware

class RazerCortex(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'RazerCortexInstaller.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://rzr.to/cortex-download')
