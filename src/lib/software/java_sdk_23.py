from src.lib.software import BaseSoftware, SoftwareCategory

class JavaSEDevelopmentKit23(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'java-sdk-23'
        self.name = 'Java SE Development Kit 23.x'
        self.category = SoftwareCategory.Development
        self.download_name = 'jdk-23_windows-x64_bin.msi'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'java.png'
        self.homepage = 'https://oracle.com/java/technologies/downloads'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.oracle.com/java/23/latest/jdk-23_windows-x64_bin.msi')
