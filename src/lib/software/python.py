from src.lib.software.variants.python_313 import Python313
from src.lib.software.variants.python_312 import Python312
from src.lib.software import BaseSoftware, SoftwareCategory

class Python(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'python'
        self.name = 'Python'
        self.category = [SoftwareCategory.Development]
        self.variants = [Python313(), Python312()]
        self.icon = 'python.png'
        self.homepage = 'https://python.org'

    def resolve_download_url(self):
        pass
