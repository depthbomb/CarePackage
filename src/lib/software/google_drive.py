from src.lib.software import BaseSoftware

class GoogleDrive(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'GoogleDriveSetup.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://dl.google.com/drive-file-stream/GoogleDriveSetup.exe')
