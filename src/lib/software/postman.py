from src.lib.software import BaseSoftware

class Postman(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'Postman-win64-Setup.exe'
        self.silent_install_args = ['--silent']

    def resolve_download_url(self):
        self.url_resolved.emit('https://dl.pstmn.io/download/latest/win64')
