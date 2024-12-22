from src.lib.software import BaseSoftware, SoftwareCategory

class DotNet9Sdk(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'dotnet-9-sdk'
        self.name = '.NET 9.0 SDK'
        self.category = SoftwareCategory.DotNet
        self.download_name = 'dotnet-sdk-9.0-win-x64.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'dotnet.png'
        self.homepage = 'https://dot.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.visualstudio.microsoft.com/download/pr/38e45a81-a6a4-4a37-a986-bc46be78db16/33e64c0966ebdf0088d1a2b6597f62e5/dotnet-sdk-9.0.101-win-x64.exe')
