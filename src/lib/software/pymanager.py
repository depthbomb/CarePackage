from src.lib.software import BaseSoftware

class PyManager(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'Python Install Manager Installer.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://get.microsoft.com/installer/download/9NQ7512CXL7T')
