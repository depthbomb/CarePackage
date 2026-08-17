from src.lib.software import BaseSoftware

class WhatsApp(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'WhatsApp Installer.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://get.microsoft.com/installer/download/9NKSQGP7F2NH')
