from src.lib.software import BaseSoftware, SoftwareCategory

class StreamlabsDesktop(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'streamlabs-desktop'
        self.name = 'Streamlabs Desktop'
        self.category = [SoftwareCategory.Media]
        self.download_name = 'Streamlabs+Desktop+Setup.exe'
        self.requires_admin = True
        self.icon = 'streamlabs-desktop.png'
        self.homepage = 'https://streamlabs.com/streamlabs-live-streaming-software'

    def resolve_download_url(self):
        self.url_resolved.emit('https://streamlabs.com/streamlabs-desktop/download?sdb=0')
