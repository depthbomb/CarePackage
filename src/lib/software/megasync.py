from src.lib.software import BaseSoftware

class Megasync(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'MEGAsyncSetup64.exe'
        self.silent_install_args = ['/S']

    def resolve_download_url(self):
        self.url_resolved.emit('https://mega.nz/MEGAsyncSetup64.exe')
