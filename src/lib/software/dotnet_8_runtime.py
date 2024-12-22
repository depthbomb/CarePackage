from src.lib.software import BaseSoftware, SoftwareCategory

class DotNet8Runtime(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'dotnet-8-runtime'
        self.name = '.NET 8.0 Runtime'
        self.category = SoftwareCategory.DotNet
        self.download_name = 'dotnet-runtime-8.0-win-x64.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'dotnet.png'
        self.homepage = 'https://dot.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.visualstudio.microsoft.com/download/pr/53e9e41c-b362-4598-9985-45f989518016/53c5e1919ba2fe23273f2abaff65595b/dotnet-runtime-8.0.11-win-x64.exe')
