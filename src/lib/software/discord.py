from src.lib.software import BaseSoftware, SoftwareCategory

class Discord(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'discord-stable'
        self.name = 'Discord'
        self.category = SoftwareCategory.Social
        self.download_name = 'DiscordSetup.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'discord.png'
        self.homepage = 'https://discord.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64')
