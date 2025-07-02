from src.lib.software import BaseSoftware

class JavaSEDevelopmentKit24(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'java-sdk-24'
        self.name = 'Java SE Development Kit 24.x'
        self.download_name = 'jdk-24_windows-x64_bin.msi'
        self.icon = 'java.png'
        self.homepage = 'https://oracle.com/java/technologies/downloads'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.oracle.com/java/24/latest/jdk-24_windows-x64_bin.msi')
