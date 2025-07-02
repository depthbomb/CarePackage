from src.lib.software import BaseSoftware, SoftwareCategory

class MelonDs(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'melonds'
        self.name = 'melonDS'
        self.category = [SoftwareCategory.Emulation, SoftwareCategory.Gaming]
        self.download_name = 'melonDS-windows-x86_64.zip'
        self.is_archive = True
        self.icon = 'melonds.png'
        self.homepage = 'https://melonds.kuribo64.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://melonds.kuribo64.net/downloads/melonDS-windows-x86_64.zip')
