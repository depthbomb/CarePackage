from src.lib.software import BaseSoftware, SoftwareCategory

class DotNet6Sdk(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'dotnet-6-sdk'
        self.name = '.NET 6.0 SDK'
        self.category = SoftwareCategory.DotNet
        self.download_name = 'dotnet-sdk-6.0-win-x64.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'dotnet.png'
        self.homepage = 'https://dot.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.visualstudio.microsoft.com/download/pr/396abf58-60df-4892-b086-9ed9c7a914ba/eb344c08fa7fc303f46d6905a0cb4ea3/dotnet-sdk-6.0.428-win-x64.exe')
