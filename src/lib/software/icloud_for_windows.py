from src.lib.software import BaseSoftware

class ICloudForWindows(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'iCloud Installer.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://get.microsoft.com/installer/download/9PKTQ5699M62')
