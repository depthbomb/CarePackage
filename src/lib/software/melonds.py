from src.lib.software import BaseSoftware

class MelonDs(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'melonDS-windows-x86_64.zip'

    def resolve_download_url(self):
        self.url_resolved.emit('https://melonds.kuribo64.net/downloads/melonDS-windows-x86_64.zip')
