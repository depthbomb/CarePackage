from src.lib.software import BaseSoftware, SoftwareCategory

class MicrosoftEdge(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'microsoft-edge'
        self.name = 'Microsoft Edge'
        self.category = [SoftwareCategory.Browser]
        self.download_name = 'MicrosoftEdgeSetup.exe'
        self.icon = 'microsoft-edge.png'
        self.homepage = 'https://microsoft.com/en-us/edge'

    def resolve_download_url(self):
        self.url_resolved.emit('https://c2rsetup.officeapps.live.com/c2r/downloadEdge.aspx?platform=Default&source=EdgeStablePage&Channel=Stable&language=en&brand=M100')
