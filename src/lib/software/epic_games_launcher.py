from src.lib.software import BaseSoftware

class EpicGamesLauncher(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'EpicGamesLauncherInstaller.msi'

    def resolve_download_url(self):
        self.url_resolved.emit('https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi')
