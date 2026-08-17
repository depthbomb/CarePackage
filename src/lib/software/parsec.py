from src.lib.software import BaseSoftware

class Parsec(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'parsec-windows.exe'
        self.silent_install_args = ['/S']

    def resolve_download_url(self):
        self.url_resolved.emit('https://builds.parsec.app/package/parsec-windows.exe')
