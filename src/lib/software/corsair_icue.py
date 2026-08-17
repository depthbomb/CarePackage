from src.lib.software import BaseSoftware

class CorsairIcue(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'Install_iCue.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://www3.corsair.com/software/CUE_V5/public/modules/windows/installer/Install%20iCUE.exe')
