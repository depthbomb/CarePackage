from src.lib.software import BaseSoftware, SoftwareCategory

class DockerDesktop(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'docker-desktop'
        self.name = 'Docker Desktop'
        self.category = SoftwareCategory.Development
        self.download_name = 'Docker Desktop Installer.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'docker-desktop.png'
        self.homepage = 'https://docker.com/products/docker-desktop'

    def resolve_download_url(self):
        self.url_resolved.emit('https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe')
