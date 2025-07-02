from src.lib.software import BaseSoftware, SoftwareCategory

class Arc(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'arc'
        self.name = 'Arc'
        self.category = [SoftwareCategory.Browser]
        self.download_name = 'ArcInstaller.exe'
        self.icon = 'arc.png'
        self.homepage = 'https://arc.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://releases.arc.net/windows/ArcInstaller.exe')
