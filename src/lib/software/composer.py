from src.lib.software import BaseSoftware

class Composer(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'Composer-Setup.exe'
        self.silent_install_args = ['/VERYSILENT', '/SUPPRESSMSGBOXES', '/NORESTART', '/SP-']

    def resolve_download_url(self):
        self.url_resolved.emit('https://getcomposer.org/Composer-Setup.exe')
