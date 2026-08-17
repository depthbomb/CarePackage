from src.lib.software import BaseSoftware

class MicrosoftEdge(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'MicrosoftEdgeSetup.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://c2rsetup.officeapps.live.com/c2r/downloadEdge.aspx?platform=Default&source=EdgeStablePage&Channel=Stable&language=en&brand=M100')
