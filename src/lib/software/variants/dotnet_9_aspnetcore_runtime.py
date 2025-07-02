from src.lib.software import BaseSoftware

class DotNet9AspNetCoreRuntime(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'dotnet-9-aspnet-core-runtime'
        self.name = '.NET 9.0 ASP.NET Core Runtime'
        self.download_name = 'aspnetcore-runtime-9.0-win-x64.exe'
        self.icon = 'dotnet.png'
        self.homepage = 'https://dot.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.visualstudio.microsoft.com/download/pr/815e6104-b92c-4cd5-8971-cba2f685002a/37befaa217f3269a152016da80a922c1/aspnetcore-runtime-9.0.0-win-x64.exe')
