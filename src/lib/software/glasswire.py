from src.lib.software import BaseSoftware, SoftwareCategory

class GlassWire(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'glasswire'
        self.name = 'GlassWire'
        self.category = [SoftwareCategory.Network, SoftwareCategory.Utility]
        self.download_name = 'GlassWireSetup.exe'
        self.is_archive = False
        self.requires_admin = True
        self.icon = 'glasswire.png'
        self.homepage = 'https://glasswire.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.glasswire.com/GlassWireSetup.exe')
