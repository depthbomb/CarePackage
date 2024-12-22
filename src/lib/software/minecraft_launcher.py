from src.lib.software import BaseSoftware, SoftwareCategory

class MinecraftLauncher(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'minecraft-launcher'
        self.name = 'Minecraft Launcher'
        self.category = SoftwareCategory.Gaming
        self.download_name = 'MinecraftInstaller.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'minecraft-launcher.png'
        self.homepage = 'https://minecraft.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://launcher.mojang.com/download/MinecraftInstaller.exe?ref=mcnet')
