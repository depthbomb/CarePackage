from src.lib.software import BaseSoftware

class LogitechGHub(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'lghub_installer.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download01.logi.com/web/ftp/pub/techsupport/gaming/lghub_installer.exe')
