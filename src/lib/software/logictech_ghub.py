from src.lib.software import BaseSoftware, SoftwareCategory

class LogitechGHub(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'logitech-g-hub'
        self.name = 'Logitech G HUB'
        self.category = [SoftwareCategory.Peripheral]
        self.download_name = 'lghub_installer.exe'
        self.icon = 'logitech-g-hub.png'
        self.homepage = 'https://www.logitechg.com/en-us/innovation/g-hub.html'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download01.logi.com/web/ftp/pub/techsupport/gaming/lghub_installer.exe')
