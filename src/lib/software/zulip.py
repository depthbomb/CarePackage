from src.lib.software import BaseSoftware

class Zulip(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'Zulip-Web-Setup.exe'
        self.silent_install_args = ['/S']

    def resolve_download_url(self):
        self.url_resolved.emit('https://zulip.com/apps/download/windows')
