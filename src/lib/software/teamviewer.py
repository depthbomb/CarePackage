from src.lib.software import BaseSoftware

class TeamViewer(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'TeamViewer_Setup_x64.exe'
        self.silent_install_args = ['/S']

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.teamviewer.com/download/TeamViewer_Setup_x64.exe')
