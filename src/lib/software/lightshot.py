from src.lib.software import BaseSoftware

class Lightshot(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'setup-lightshot.exe'
        self.silent_install_args = ['/VERYSILENT', '/SUPPRESSMSGBOXES', '/NORESTART', '/SP-']

    def resolve_download_url(self):
        self.url_resolved.emit('https://app.prntscr.com/build/setup-lightshot.exe')
