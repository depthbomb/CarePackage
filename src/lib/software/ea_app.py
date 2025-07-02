from src.lib.software import BaseSoftware, SoftwareCategory

class EaApp(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'ea-app'
        self.name = 'EA App'
        self.category = [SoftwareCategory.Gaming]
        self.download_name = 'EAappInstaller.exe'
        self.icon = 'ea-app.png'
        self.homepage = 'https://ea.com/ea-app'

    def resolve_download_url(self):
        self.url_resolved.emit('https://origin-a.akamaihd.net/EA-Desktop-Client-Download/installer-releases/EAappInstaller.exe')
