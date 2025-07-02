from src.lib.software import BaseSoftware, SoftwareCategory

class OneDrive(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'onedrive'
        self.name = 'OneDrive'
        self.category = SoftwareCategory.Utility
        self.download_name = 'OneDriveSetup.exe'
        self.icon = 'onedrive.png'
        self.homepage = 'https://www.microsoft.com/en-us/microsoft-365/onedrive'

    def resolve_download_url(self):
        self.url_resolved.emit('https://go.microsoft.com/fwlink/?linkid=844652')
