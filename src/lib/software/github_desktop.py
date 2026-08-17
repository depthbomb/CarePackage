from src.lib.software import BaseSoftware

class GitHubDesktop(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'GitHubDesktopSetup-x64.exe'
        self.silent_install_args = ['--silent']

    def resolve_download_url(self):
        self.url_resolved.emit('https://central.github.com/deployments/desktop/desktop/latest/win32')
