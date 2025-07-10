from src.lib.software import BaseSoftware, SoftwareCategory

class Calibre(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'calibre'
        self.name = 'calibre'
        self.category = [SoftwareCategory.Media]
        self.download_name = 'calibre-64bit.msi'
        self.icon = 'calibre.png'
        self.homepage = 'https://calibre-ebook.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://calibre-ebook.com/dist/win64')
