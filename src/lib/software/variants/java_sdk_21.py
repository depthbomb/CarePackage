from src.lib.software import BaseSoftware

class JavaSEDevelopmentKit21(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'java-sdk-21'
        self.name = 'Java SE Development Kit 21.x'
        self.download_name = 'jdk-21_windows-x64_bin.msi'
        self.icon = 'java.png'
        self.homepage = 'https://oracle.com/java/technologies/downloads'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.oracle.com/java/21/latest/jdk-21_windows-x64_bin.msi')
