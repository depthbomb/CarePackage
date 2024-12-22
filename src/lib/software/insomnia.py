from src.lib.software import BaseSoftware, SoftwareCategory

class Insomnia(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'insomnia'
        self.name = 'Insomnia'
        self.category = SoftwareCategory.Development
        self.download_name = 'Insomnia.Core.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'insomnia.png'
        self.homepage = 'https://insomnia.rest'

    def resolve_download_url(self):
        self.url_resolved.emit('https://updates.insomnia.rest/downloads/windows/latest?app=com.insomnia.app&source=website')
