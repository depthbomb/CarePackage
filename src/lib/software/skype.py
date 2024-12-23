from src.lib.software import BaseSoftware, SoftwareCategory

class Skype(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'skype'
        self.name = 'Skype'
        self.category = SoftwareCategory.Social
        self.download_name = 'Skype.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'skype.png'
        self.homepage = 'https://www.skype.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://get.skype.com/go/getskype-skypeforwindows')
