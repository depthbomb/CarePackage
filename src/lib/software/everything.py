from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.software.variants.everything_cli import EverythingCLI
from src.lib.software.variants.everything_lite import EverythingLite
from src.lib.software.variants.everything_standard import EverythingStandard

class Everything(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'everything'
        self.name = 'Everything'
        self.category = [SoftwareCategory.Utility]
        self.variants = [EverythingStandard(), EverythingLite(), EverythingCLI()]
        self.icon = 'everything.png'
        self.homepage = 'https://voidtools.com'

    def resolve_download_url(self):
        pass
