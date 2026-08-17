from src.lib.software import BaseSoftware

class VisualStudioCommunity(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'VisualStudioSetup.exe'
        self.should_cache_url = True

    def resolve_download_url(self):
        self.url_resolved.emit('https://c2rsetup.officeapps.live.com/c2r/downloadVS.aspx?sku=community&channel=stable&version=VS18&source=VSLandingPage')
