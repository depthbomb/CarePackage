from src.lib.software import BaseSoftware, SoftwareCategory

class WeMod(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'wemod'
        self.name = 'WeMod'
        self.category = [SoftwareCategory.Gaming, SoftwareCategory.Utility]
        self.download_name = 'WeMod-Setup.exe'
        self.icon = 'wemod.png'
        self.homepage = 'https://wemod.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://www.wemod.com/download/direct')
