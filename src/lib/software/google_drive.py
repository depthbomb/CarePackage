from src.lib.software import BaseSoftware, SoftwareCategory

class GoogleDrive(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'google-drive'
        self.name = 'Google Drive'
        self.category = [SoftwareCategory.FileManagement, SoftwareCategory.Utility]
        self.download_name = 'GoogleDriveSetup.exe'
        self.icon = 'google-drive.png'
        self.homepage = 'https://workspace.google.com/products/drive'

    def resolve_download_url(self):
        self.url_resolved.emit('https://dl.google.com/drive-file-stream/GoogleDriveSetup.exe')
