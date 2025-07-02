from src.lib.software import BaseSoftware, SoftwareCategory

class MozillaFirefox(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'mozilla-firefox'
        self.name = 'Mozilla Firefox'
        self.category = [SoftwareCategory.Browser]
        self.download_name = 'Firefox Installer.exe'
        self.icon = 'mozilla-firefox.png'
        self.homepage = 'https://mozilla.org/firefox'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=en-US')
