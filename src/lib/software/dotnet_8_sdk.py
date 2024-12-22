from src.lib.software import BaseSoftware, SoftwareCategory

class DotNet8Sdk(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'dotnet-8-sdk'
        self.name = '.NET 8.0 SDK'
        self.category = SoftwareCategory.DotNet
        self.download_name = 'dotnet-sdk-8.0-win-x64.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'dotnet.png'
        self.homepage = 'https://dot.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.visualstudio.microsoft.com/download/pr/ba3a1364-27d8-472e-a33b-5ce0937728aa/6f9495e5a587406c85af6f93b1c89295/dotnet-sdk-8.0.404-win-x64.exe')
