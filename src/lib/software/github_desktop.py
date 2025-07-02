from src.lib.software import BaseSoftware, SoftwareCategory

class GitHubDesktop(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'github-desktop'
        self.name = 'GitHub Desktop'
        self.category = [SoftwareCategory.Development]
        self.download_name = 'GitHubDesktopSetup-x64.exe'
        self.icon = 'github-desktop.png'
        self.homepage = 'https://desktop.github.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://central.github.com/deployments/desktop/desktop/latest/win32')
