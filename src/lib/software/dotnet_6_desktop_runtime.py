from src.lib.software import BaseSoftware, SoftwareCategory

class DotNet6DesktopRuntime(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'dotnet-6-desktop-runtime'
        self.name = '.NET 6.0 Desktop Runtime'
        self.category = SoftwareCategory.DotNet
        self.download_name = 'windowsdesktop-runtime-6.0-win-x64.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'dotnet.png'
        self.homepage = 'https://dot.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.visualstudio.microsoft.com/download/pr/f6b6c5dc-e02d-4738-9559-296e938dabcb/b66d365729359df8e8ea131197715076/windowsdesktop-runtime-6.0.36-win-x64.exe')
