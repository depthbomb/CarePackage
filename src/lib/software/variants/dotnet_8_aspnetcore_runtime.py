from src.lib.software import BaseSoftware

class DotNet8AspNetCoreRuntime(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'dotnet-8-aspnet-core-runtime'
        self.name = '.NET 8.0 ASP.NET Core Runtime'
        self.download_name = 'aspnetcore-runtime-8.0-win-x64.exe'
        self.icon = 'dotnet.png'
        self.homepage = 'https://dot.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.visualstudio.microsoft.com/download/pr/8d6c1aaa-7d58-455a-acec-aab350860582/ab5f7c23dc72516e77065fcaf99ad444/aspnetcore-runtime-8.0.11-win-x64.exe')
