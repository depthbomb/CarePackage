from src.lib.software import BaseSoftware

class MinecraftLauncherLegacy(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'minecraft-launcher-legacy'
        self.name = 'Minecraft Launcher (Legacy)'
        self.download_name = 'MinecraftInstaller.msi'
        self.icon = 'minecraft-launcher-legacy.png'
        self.homepage = 'https://minecraft.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://launcher.mojang.com/download/MinecraftInstaller.msi?ref=mcnet')
