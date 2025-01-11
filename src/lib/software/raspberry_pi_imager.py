from src.lib.software import BaseSoftware, SoftwareCategory

class RaspberryPiImager(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'raspberry-pi-imager'
        self.name = 'Raspberry Pi Imager'
        self.category = SoftwareCategory.Utility
        self.download_name = 'imager_latest.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = True
        self.icon = 'raspberry-pi-imager.png'
        self.homepage = 'https://raspberrypi.com/software'

    def resolve_download_url(self):
        self.url_resolved.emit('https://downloads.raspberrypi.org/imager/imager_latest.exe')
