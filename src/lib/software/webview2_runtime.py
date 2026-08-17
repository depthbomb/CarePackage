from src.lib.software import BaseSoftware

class WebView2Runtime(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'MicrosoftEdgeWebview2Setup.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://go.microsoft.com/fwlink/p/?LinkId=2124703')
