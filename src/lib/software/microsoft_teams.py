from src.lib.software import BaseSoftware

class MicrosoftTeams(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'MSTeamsSetup.exe'
        self.silent_install_args = ['--silent']

    def resolve_download_url(self):
        self.url_resolved.emit('https://go.microsoft.com/fwlink/?linkid=2281613&clcid=0x409&culture=en-us&country=us')
