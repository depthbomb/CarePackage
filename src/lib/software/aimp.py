from src.lib.software import BaseSoftware, SoftwareCategory

class Aimp(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'aimp'
        self.name = 'AIMP'
        self.category = [SoftwareCategory.Audio, SoftwareCategory.Media]
        self.download_name = 'aimp_w64.exe'
        self.should_cache_url = True
        self.icon = 'aimp.png'
        self.homepage = 'https://aimp.ru'

    def resolve_download_url(self):
        self.url_resolved.emit('https://www.aimp.ru/?do=download.file&id=3')
