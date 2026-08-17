from src.lib.software import BaseSoftware

class EaApp(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'EAappInstaller.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://origin-a.akamaihd.net/EA-Desktop-Client-Download/installer-releases/EAappInstaller.exe')
