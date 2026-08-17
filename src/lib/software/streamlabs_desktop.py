from src.lib.software import BaseSoftware

class StreamlabsDesktop(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'Streamlabs+Desktop+Setup.exe'
        self.silent_install_args = ['/S']

    def resolve_download_url(self):
        self.url_resolved.emit('https://streamlabs.com/streamlabs-desktop/download?sdb=0')
