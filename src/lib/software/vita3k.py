from src.lib.software import BaseSoftware, SoftwareCategory

class Vita3k(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'vita3k'
        self.name = 'Vita3K'
        self.category = [SoftwareCategory.Emulation, SoftwareCategory.Gaming]
        self.download_name = 'vita3k-windows-latest.zip'
        self.is_archive = True
        self.icon = 'vita3k.png'
        self.homepage = 'https://vita3k.org'

    def resolve_download_url(self):
        self.url_resolved.emit('https://github.com/Vita3K/Vita3K/releases/download/continuous/windows-latest.zip')
