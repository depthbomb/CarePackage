from src.lib.software import BaseSoftware

class InnoSetup(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'innosetup.exe'
        self.silent_install_args = ['/VERYSILENT', '/SUPPRESSMSGBOXES', '/NORESTART', '/SP-']

    def resolve_download_url(self):
        self.url_resolved.emit('https://jrsoftware.org/download.php/is.exe?site=1')
