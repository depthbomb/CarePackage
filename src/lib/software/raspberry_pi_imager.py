from src.lib.software import BaseSoftware

class RaspberryPiImager(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'imager_latest.exe'
        self.silent_install_args = ['/VERYSILENT', '/SUPPRESSMSGBOXES', '/NORESTART', '/SP-']

    def resolve_download_url(self):
        self.url_resolved.emit('https://downloads.raspberrypi.org/imager/imager_latest.exe')
