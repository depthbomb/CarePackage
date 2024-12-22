from src.lib.software import BaseSoftware, SoftwareCategory

class CorsairIcue(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'corsair-icue'
        self.name = 'Corsair iCUE'
        self.category = SoftwareCategory.Peripheral
        self.download_name = 'Install_iCue.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = True
        self.icon = 'corsair-icue.png'
        self.homepage = 'https://corsair.com/us/en/s/icue'

    def resolve_download_url(self):
        self.url_resolved.emit('https://www3.corsair.com/software/CUE_V5/public/modules/windows/installer/Install%20iCUE.exe')
