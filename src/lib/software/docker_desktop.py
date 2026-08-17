from src.lib.software import BaseSoftware

class DockerDesktop(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'Docker Desktop Installer.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe')
