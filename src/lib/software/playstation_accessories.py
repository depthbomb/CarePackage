from src.lib.software import BaseSoftware, SoftwareCategory

class PlayStationAccessories(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'playstation-accessories'
        self.name = 'PlayStation Accessories'
        self.category = [SoftwareCategory.Gaming, SoftwareCategory.Peripheral]
        self.download_name = 'PlayStationAccessoriesInstaller.exe'
        self.icon = 'playstation-accessories.png'
        self.homepage = 'https://controller.dl.playstation.net/controller/lang/en/2100004.html'

    def resolve_download_url(self):
        self.url_resolved.emit('https://fwupdater.dl.playstation.net/fwupdater/PlayStationAccessoriesInstaller.exe')
