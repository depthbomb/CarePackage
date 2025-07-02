from src.lib.software import BaseSoftware, SoftwareCategory

class Megasync(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'megasync'
        self.name = 'MEGAsync'
        self.category = [SoftwareCategory.FileManagement, SoftwareCategory.Utility]
        self.download_name = 'MEGAsyncSetup64.exe'
        self.is_archive = False
        self.icon = 'megasync.png'
        self.homepage = 'https://mega.io/desktop'

    def resolve_download_url(self):
        self.url_resolved.emit('https://mega.nz/MEGAsyncSetup64.exe')
