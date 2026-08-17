from src.lib.software import BaseSoftware

class Notion(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'Notion Setup.exe'
        self.silent_install_args = ['/S']

    def resolve_download_url(self):
        self.url_resolved.emit('https://www.notion.com/desktop/windows/download')
