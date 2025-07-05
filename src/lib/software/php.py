from src.lib.software.variants.php_ts import PHPTS
from src.lib.software.variants.php_nts import PHPNTS
from src.lib.software import BaseSoftware, SoftwareCategory

class PHP(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'php'
        self.name = 'PHP'
        self.category = [SoftwareCategory.Development, SoftwareCategory.Runtime]
        self.variants = [PHPNTS(), PHPTS()]
        self.icon = 'php.png'
        self.homepage = 'https://php.net'

    def resolve_download_url(self):
        pass
