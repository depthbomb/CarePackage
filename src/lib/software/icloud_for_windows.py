from src.lib.software import BaseSoftware, SoftwareCategory

class ICloudForWindows(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'icloud-for-windows'
        self.name = 'iCloud for Windows'
        self.category = [SoftwareCategory.FileManagement]
        self.download_name = 'iCloud Installer.exe'
        self.icon = 'icloud.png'
        self.homepage = 'https://support.apple.com/en-us/103232'

    def resolve_download_url(self):
        self.url_resolved.emit('https://get.microsoft.com/installer/download/9PKTQ5699M62')
