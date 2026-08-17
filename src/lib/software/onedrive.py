from src.lib.software import BaseSoftware

class OneDrive(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'OneDriveSetup.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://go.microsoft.com/fwlink/?linkid=844652')
