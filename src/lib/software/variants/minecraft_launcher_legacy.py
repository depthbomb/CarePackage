from src.lib.software import BaseSoftware

class MinecraftLauncherLegacy(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'MinecraftInstaller.msi'

    def resolve_download_url(self):
        self.url_resolved.emit('https://launcher.mojang.com/download/MinecraftInstaller.msi?ref=mcnet')
