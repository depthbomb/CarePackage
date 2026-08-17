from src.lib.software import BaseSoftware

class DotNet9Sdk(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'dotnet-sdk-9.0-win-x64.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://aka.ms/dotnet/9.0/dotnet-sdk-win-x64.exe')
