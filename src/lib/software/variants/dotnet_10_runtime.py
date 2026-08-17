from src.lib.software import BaseSoftware

class DotNet10Runtime(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'dotnet-runtime-10.0-win-x64.exe'
        self.silent_install_args = ['/install', '/quiet', '/norestart']

    def resolve_download_url(self):
        self.url_resolved.emit('https://aka.ms/dotnet/10.0/dotnet-runtime-win-x64.exe')
