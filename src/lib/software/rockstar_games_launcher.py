from src.lib.software import BaseSoftware, SoftwareCategory

class RockstarGamesLauncher(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'rockstar-games-launcher'
        self.name = 'Rockstar Games Launcher'
        self.category = [SoftwareCategory.Gaming]
        self.download_name = 'Rockstar-Games-Launcher.exe'
        self.icon = 'rockstar-games-launcher.png'
        self.homepage = 'https://socialclub.rockstargames.com/rockstar-games-launcher'

    def resolve_download_url(self):
        self.url_resolved.emit('https://gamedownloads.rockstargames.com/public/installer/Rockstar-Games-Launcher.exe')
