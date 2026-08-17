from src.lib.software import BaseSoftware

class DotNet9DesktopRuntime(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'windowsdesktop-runtime-9.0-win-x64.exe'
        self.silent_install_args = ['/install', '/quiet', '/norestart']

    def resolve_download_url(self):
        self.url_resolved.emit('https://aka.ms/dotnet/9.0/windowsdesktop-runtime-win-x64.exe')
