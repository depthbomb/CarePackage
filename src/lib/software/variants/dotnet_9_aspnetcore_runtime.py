from src.lib.software import BaseSoftware

class DotNet9AspNetCoreRuntime(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'aspnetcore-runtime-9.0-win-x64.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://aka.ms/dotnet/9.0/aspnetcore-runtime-win-x64.exe')
