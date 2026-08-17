from src.lib.software import BaseSoftware

class JavaSEDevelopmentKit25(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'jdk-25_windows-x64_bin.msi'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.oracle.com/java/25/latest/jdk-25_windows-x64_bin.msi')
