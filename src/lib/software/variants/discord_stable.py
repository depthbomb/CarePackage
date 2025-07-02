from src.lib.software import BaseSoftware

class DiscordStable(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'discord-stable'
        self.name = 'Discord Stable'
        self.download_name = 'DiscordSetup.exe'
        self.icon = 'discord.png'
        self.homepage = 'https://discord.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64')
