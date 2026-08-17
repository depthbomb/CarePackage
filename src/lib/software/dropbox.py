from src.lib.software import BaseSoftware

class Dropbox(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'DropoboxInstaller.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://www.dropbox.com/download?os=win&plat=win')
