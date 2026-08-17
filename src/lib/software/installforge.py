from src.lib.software import BaseSoftware

class InstallForge(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'IFSetup.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://installforge.net/downloads/?i=IFSetup')
