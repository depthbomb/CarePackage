from src.lib.software import BaseSoftware, SoftwareCategory

class WhatsApp(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'whatsapp'
        self.name = 'WhatsApp'
        self.category = [SoftwareCategory.Social]
        self.download_name = 'WhatsApp Installer.exe'
        self.icon = 'whatsapp.png'
        self.homepage = 'https://whatsapp.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://get.microsoft.com/installer/download/9NKSQGP7F2NH')
