from src.lib.software import BaseSoftware

class RockstarGamesLauncher(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'Rockstar-Games-Launcher.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://gamedownloads.rockstargames.com/public/installer/Rockstar-Games-Launcher.exe')
