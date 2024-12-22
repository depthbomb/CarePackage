from src.lib.software import BaseSoftware, SoftwareCategory

class DotNet6AspNetCoreRuntime(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'dotnet-6-aspnet-core-runtime'
        self.name = '.NET 6.0 ASP.NET Core Runtime'
        self.category = SoftwareCategory.DotNet
        self.download_name = 'aspnetcore-runtime-6.0-win-x64.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'dotnet.png'
        self.homepage = 'https://dot.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.visualstudio.microsoft.com/download/pr/0f0ea01c-ef7c-4493-8960-d1e9269b718b/3f95c5bd383be65c2c3384e9fa984078/aspnetcore-runtime-6.0.36-win-x64.exe')
