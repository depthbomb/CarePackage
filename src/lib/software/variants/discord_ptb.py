from src.lib.software import BaseSoftware

class DiscordPtb(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'discord-ptb'
        self.name = 'Discord PTB'
        self.download_name = 'DiscordPTBSetup.exe'
        self.icon = 'discord.png'
        self.homepage = 'https://ptb.discord.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://ptb.discord.com/api/downloads/distributions/app/installers/latest?channel=ptb&platform=win&arch=x64')
