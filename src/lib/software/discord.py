from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.software.variants.discord_ptb import DiscordPtb
from src.lib.software.variants.discord_stable import DiscordStable
from src.lib.software.variants.discord_canary import DiscordCanary

class Discord(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'discord'
        self.name = 'Discord'
        self.category = [SoftwareCategory.Social]
        self.variants = [DiscordStable(), DiscordPtb(), DiscordCanary()]
        self.icon = 'discord.png'
        self.homepage = 'https://discord.com'

    def resolve_download_url(self):
        pass
