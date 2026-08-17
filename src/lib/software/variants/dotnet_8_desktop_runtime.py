from src.lib.software import BaseSoftware

class DotNet8DesktopRuntime(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'windowsdesktop-runtime-8.0-win-x64.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://aka.ms/dotnet/8.0/windowsdesktop-runtime-win-x64.exe')
