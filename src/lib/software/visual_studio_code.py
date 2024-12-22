from src.lib.software import BaseSoftware, SoftwareCategory

class VisualStudioCode(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'visual-studio-code'
        self.name = 'Visual Studio Code'
        self.category = SoftwareCategory.Development
        self.download_name = 'VSCodeUserSetup-x64.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'visual-studio-code.png'
        self.homepage = 'https://code.visualstudio.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user')
