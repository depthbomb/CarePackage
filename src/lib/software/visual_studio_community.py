from src.lib.software import BaseSoftware, SoftwareCategory

class VisualStudioCommunity(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'visual-studio-community'
        self.name = 'Visual Studio 2026 Community'
        self.category = [SoftwareCategory.Development]
        self.download_name = 'VisualStudioSetup.exe'
        self.should_cache_url = True
        self.icon = 'visual-studio-community.png'
        self.homepage = 'https://visualstudio.microsoft.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://c2rsetup.officeapps.live.com/c2r/downloadVS.aspx?sku=community&channel=stable&version=VS18&source=VSLandingPage')
