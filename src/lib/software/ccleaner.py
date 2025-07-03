from src.lib.software import BaseSoftware, SoftwareCategory

class Ccleaner(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'ccleaner'
        self.name = 'CCleaner'
        self.category = [SoftwareCategory.FileManagement, SoftwareCategory.SystemManagement, SoftwareCategory.Utility]
        self.download_name = 'ccsetup.exe'
        self.icon = 'ccleaner.png'
        self.homepage = 'https://ccleaner.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://bits.avcdn.net/productfamily_CCLEANER/insttype_FREE/platform_WIN_PIR/installertype_ONLINE/build_RELEASE')
