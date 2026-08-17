from src.lib.software import BaseSoftware

class Calibre(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'calibre-64bit.msi'

    def resolve_download_url(self):
        self.url_resolved.emit('https://calibre-ebook.com/dist/win64')
