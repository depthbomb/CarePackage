from src.lib.software import BaseSoftware

class DotNet10Sdk(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'dotnet-sdk-10.0-win-x64.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://aka.ms/dotnet/10.0/dotnet-sdk-win-x64.exe')
