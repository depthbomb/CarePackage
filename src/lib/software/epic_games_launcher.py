from src.lib.software import BaseSoftware, SoftwareCategory

class EpicGamesLauncher(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'epic-games-launcher'
        self.name = 'Epic Games Launcher'
        self.category = SoftwareCategory.Gaming
        self.download_name = 'EpicGamesLauncherInstaller.msi'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'epic-games-launcher.png'
        self.homepage = 'https://store.epicgames.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi')
