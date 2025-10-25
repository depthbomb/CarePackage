from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.software.variants.temurin_jdk_8 import TemurinJDK8
from src.lib.software.variants.temurin_jdk_11 import TemurinJDK11
from src.lib.software.variants.temurin_jdk_17 import TemurinJDK17
from src.lib.software.variants.temurin_jdk_21 import TemurinJDK21
from src.lib.software.variants.temurin_jdk_25 import TemurinJDK25

# TODO Use the Adoptium API

class TemurinJDK(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'temurin-jdk'
        self.name = 'Temurin JDK'
        self.category = [SoftwareCategory.Development, SoftwareCategory.Runtime]
        self.variants = [TemurinJDK8(), TemurinJDK11(), TemurinJDK17(), TemurinJDK21(), TemurinJDK25()]
        self.icon = 'temurin.png'
        self.homepage = 'https://adoptium.net'

    def resolve_download_url(self):
        pass
