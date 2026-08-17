from src.lib.software import BaseSoftware

class Ccleaner(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'ccsetup.exe'
        self.silent_install_args = ['/S']

    def resolve_download_url(self):
        self.url_resolved.emit('https://bits.avcdn.net/productfamily_CCLEANER/insttype_FREE/platform_WIN_PIR/installertype_ONLINE/build_RELEASE')
