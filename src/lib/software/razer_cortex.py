from src.lib.software import BaseSoftware, SoftwareCategory

class RazerCortex(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'razer-cortex'
        self.name = 'Razer Cortex'
        self.category = SoftwareCategory.Gaming
        self.download_name = 'RazerCortexInstaller.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = True
        self.icon = 'razer-cortex.png'
        self.homepage = 'https://razer.com/cortex'

    def resolve_download_url(self):
        self.url_resolved.emit('https://rzr.to/cortex-download')
