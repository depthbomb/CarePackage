from src.lib.software import BaseSoftware, SoftwareCategory

class TelegramDesktop(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'telegram-desktop'
        self.name = 'Telegram'
        self.category = [SoftwareCategory.Social]
        self.download_name = 'tsetup.exe'
        self.icon = 'telegram.png'
        self.homepage = 'https://telegram.org'

    def resolve_download_url(self):
        self.url_resolved.emit('https://telegram.org/dl/desktop/win64')
