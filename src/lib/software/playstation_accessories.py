from src.lib.software import BaseSoftware

class PlayStationAccessories(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'PlayStationAccessoriesInstaller.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://fwupdater.dl.playstation.net/fwupdater/PlayStationAccessoriesInstaller.exe')
