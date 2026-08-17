from src.lib.software import BaseSoftware

class Aimp(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'aimp_w64.exe'
        self.should_cache_url = True

    def resolve_download_url(self):
        self.url_resolved.emit('https://www.aimp.ru/?do=download.file&id=3')
