from src.lib.software import BaseSoftware, SoftwareCategory

class InstallForge(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'installforge'
        self.name = 'InstallForge'
        self.category = [SoftwareCategory.Development]
        self.download_name = 'IFSetup.exe'
        self.requires_admin = True
        self.icon = 'installforge.png'
        self.homepage = 'https://installforge.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://installforge.net/downloads/?i=IFSetup')
