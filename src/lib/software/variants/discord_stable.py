from src.lib.software import BaseSoftware

class DiscordStable(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'DiscordSetup.exe'
        self.silent_install_args = ['--silent']

    def resolve_download_url(self):
        self.url_resolved.emit('https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64')
