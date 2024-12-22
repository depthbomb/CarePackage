from src.lib.software import BaseSoftware, SoftwareCategory

class WebView2Runtime(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'webview2-runtime'
        self.name = 'Microsoft Edge WebView2 Runtime'
        self.category = SoftwareCategory.Runtime
        self.download_name = 'MicrosoftEdgeWebview2Setup.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'microsoft-edge-webview2-runtime.png'
        self.homepage = 'https://developer.microsoft.com/en-us/microsoft-edge/webview2'

    def resolve_download_url(self):
        self.url_resolved.emit('https://go.microsoft.com/fwlink/p/?LinkId=2124703')
