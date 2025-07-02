from src.lib.software import BaseSoftware, SoftwareCategory

class TeamViewer(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'teamviewer'
        self.name = 'TeamViewer'
        self.category = [SoftwareCategory.Social, SoftwareCategory.Utility]
        self.download_name = 'TeamViewer_Setup_x64.exe'
        self.icon = 'teamviewer.png'
        self.homepage = 'https://teamviewer.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.teamviewer.com/download/TeamViewer_Setup_x64.exe')
