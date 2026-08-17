from src.lib.software import BaseSoftware

class Vita3k(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'vita3k-windows-latest.zip'

    def resolve_download_url(self):
        self.url_resolved.emit('https://github.com/Vita3K/Vita3K/releases/download/continuous/windows-latest.zip')
