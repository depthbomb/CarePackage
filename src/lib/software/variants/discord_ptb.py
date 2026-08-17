from src.lib.software import BaseSoftware

class DiscordPtb(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'DiscordPTBSetup.exe'
        self.silent_install_args = ['--silent']

    def resolve_download_url(self):
        self.url_resolved.emit('https://ptb.discord.com/api/downloads/distributions/app/installers/latest?channel=ptb&platform=win&arch=x64')
