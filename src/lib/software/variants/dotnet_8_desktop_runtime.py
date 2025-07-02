from src.lib.software import BaseSoftware

class DotNet8DesktopRuntime(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'dotnet-8-desktop-runtime'
        self.name = '.NET 8.0 Desktop Runtime'
        self.download_name = 'windowsdesktop-runtime-8.0-win-x64.exe'
        self.icon = 'dotnet.png'
        self.homepage = 'https://dot.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.visualstudio.microsoft.com/download/pr/27bcdd70-ce64-4049-ba24-2b14f9267729/d4a435e55182ce5424a7204c2cf2b3ea/windowsdesktop-runtime-8.0.11-win-x64.exe')
