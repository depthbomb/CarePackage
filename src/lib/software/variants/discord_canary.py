from src.lib.software import BaseSoftware

class DiscordCanary(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'DiscordCanarySetup.exe'
        self.silent_install_args = ['--silent']

    def resolve_download_url(self):
        self.url_resolved.emit('https://canary.discord.com/api/downloads/distributions/app/installers/latest?channel=canary&platform=win&arch=x64')
