from src.lib.software import BaseSoftware, SoftwareCategory

class DotNet9DesktopRuntime(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'dotnet-9-desktop-runtime'
        self.name = '.NET 9.0 Desktop Runtime'
        self.category = SoftwareCategory.DotNet
        self.download_name = 'windowsdesktop-runtime-9.0-win-x64.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'dotnet.png'
        self.homepage = 'https://dot.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.visualstudio.microsoft.com/download/pr/685792b6-4827-4dca-a971-bce5d7905170/1bf61b02151bc56e763dc711e45f0e1e/windowsdesktop-runtime-9.0.0-win-x64.exe')
