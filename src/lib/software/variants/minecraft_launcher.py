from src.lib.software import BaseSoftware

class MinecraftLauncher(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'minecraft-launcher'
        self.name = 'Minecraft Launcher'
        self.download_name = 'MinecraftInstaller.exe'
        self.icon = 'minecraft-launcher.png'
        self.homepage = 'https://minecraft.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://launcher.mojang.com/download/MinecraftInstaller.exe?ref=mcnet')
