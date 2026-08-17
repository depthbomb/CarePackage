from src.lib.software import BaseSoftware

class MinecraftLauncher(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'MinecraftInstaller.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://launcher.mojang.com/download/MinecraftInstaller.exe?ref=mcnet')
