from src.lib.software.variants.nodejs_lts import NodeJsLts
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.software.variants.nodejs_current import NodeJsCurrent

class NodeJs(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'nodejs'
        self.name = 'Node.js'
        self.category = [SoftwareCategory.Development, SoftwareCategory.Runtime]
        self.variants = [NodeJsCurrent(), NodeJsLts()]
        self.icon = 'nodejs.png'
        self.homepage = 'https://nodejs.org'

    def resolve_download_url(self):
        pass
