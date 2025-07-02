from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.software.variants.minecraft_launcher import MinecraftLauncher
from src.lib.software.variants.minecraft_launcher_legacy import MinecraftLauncherLegacy

class Minecraft(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'minecraft'
        self.name = 'Minecraft'
        self.category = [SoftwareCategory.Gaming]
        self.variants = [MinecraftLauncher(), MinecraftLauncherLegacy()]
        self.icon = 'minecraft-launcher.png'
        self.homepage = 'https://minecraft.net'

    def resolve_download_url(self):
        pass
