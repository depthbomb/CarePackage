from src.lib.software import BaseSoftware, SoftwareCategory

class PyManager(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'pymanager'
        self.name = 'Python Install Manager'
        self.category = [SoftwareCategory.Development, SoftwareCategory.Runtime, SoftwareCategory.Utility]
        self.download_name = 'Python Install Manager Installer.exe'
        self.icon = 'pymanager.png'
        self.homepage = 'https://docs.python.org/3/using/windows.html'

    def resolve_download_url(self):
        self.url_resolved.emit('https://get.microsoft.com/installer/download/9NQ7512CXL7T')
