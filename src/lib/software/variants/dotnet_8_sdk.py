from src.lib.software import BaseSoftware

class DotNet8Sdk(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'dotnet-sdk-8.0-win-x64.exe'
        self.silent_install_args = ['/install', '/quiet', '/norestart']

    def resolve_download_url(self):
        self.url_resolved.emit('https://aka.ms/dotnet/8.0/dotnet-sdk-win-x64.exe')
