from src.lib.software import BaseSoftware, SoftwareCategory

class MicrosoftTeams(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'microsoft-teams'
        self.name = 'Microsoft Teams'
        self.category = SoftwareCategory.Social
        self.download_name = 'MSTeamsSetup.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'microsoft-teams.png'
        self.homepage = 'https://microsoft.com/en-us/microsoft-teams'

    def resolve_download_url(self):
        self.url_resolved.emit('https://go.microsoft.com/fwlink/?linkid=2281613&clcid=0x409&culture=en-us&country=us')
