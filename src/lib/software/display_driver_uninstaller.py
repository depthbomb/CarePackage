from src.lib.software import BaseSoftware

class DisplayDriverUninstaller(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = '[Guru3D.com]-DDU.zip'

    def resolve_download_url(self):
        self.url_resolved.emit('https://ftp.nluug.nl/pub/games/PC/guru3d/ddu/[Guru3D]-DDU.zip')
