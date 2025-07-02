from src.lib.software import BaseSoftware

class DiscordCanary(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'discord-canary'
        self.name = 'Discord Canary'
        self.download_name = 'DiscordCanarySetup.exe'
        self.icon = 'discord-canary.png'
        self.homepage = 'https://canary.discord.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://canary.discord.com/api/downloads/distributions/app/installers/latest?channel=canary&platform=win&arch=x64')
