from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.software.variants.java_sdk_21 import JavaSEDevelopmentKit21
from src.lib.software.variants.java_sdk_24 import JavaSEDevelopmentKit24

class JavaSEDevelopmentKit(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'java-sdk'
        self.name = 'Java SE Development Kit'
        self.category = [SoftwareCategory.Development, SoftwareCategory.Runtime]
        self.variants = [JavaSEDevelopmentKit24(), JavaSEDevelopmentKit21()]
        self.icon = 'java.png'
        self.homepage = 'https://oracle.com/java/technologies/downloads'

    def resolve_download_url(self):
        pass
