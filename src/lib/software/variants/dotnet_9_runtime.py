from src.lib.software import BaseSoftware

class DotNet9Runtime(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'dotnet-9-runtime'
        self.name = '.NET 9.0 Runtime'
        self.download_name = 'dotnet-runtime-9.0-win-x64.exe'
        self.icon = 'dotnet.png'
        self.homepage = 'https://dot.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.visualstudio.microsoft.com/download/pr/99bd07c2-c95c-44dc-9d47-36d3b18df240/bdf26c62f69c1b783687c1dce83ccf7a/dotnet-runtime-9.0.0-win-x64.exe')
