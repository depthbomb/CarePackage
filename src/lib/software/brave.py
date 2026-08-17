from src.lib.software import BaseSoftware

class Brave(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'BraveBrowserSetup.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://laptop-updates.brave.com/download/desktop/release/BRV010?bitness=64')
