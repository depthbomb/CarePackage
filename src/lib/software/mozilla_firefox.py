from src.lib.software import BaseSoftware

class MozillaFirefox(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'Firefox Installer.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=en-US')
