from src.lib.software import BaseSoftware

class TeraCopy(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'teracopy.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://www.codesector.com/files/teracopy.exe')
