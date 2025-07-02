from src.lib.software import BaseSoftware, SoftwareCategory

class Lightshot(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'lightshot'
        self.name = 'Lightshot'
        self.category = [SoftwareCategory.Media, SoftwareCategory.Utility]
        self.download_name = 'setup-lightshot.exe'
        self.is_archive = False
        self.icon = 'lightshot.png'
        self.homepage = 'https://app.prntscr.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://app.prntscr.com/build/setup-lightshot.exe')
