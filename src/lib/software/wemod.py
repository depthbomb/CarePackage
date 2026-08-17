from src.lib.software import BaseSoftware

class WeMod(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'WeMod-Setup.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://www.wemod.com/download/direct')
