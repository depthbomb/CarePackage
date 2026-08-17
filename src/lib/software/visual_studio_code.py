from src.lib.software import BaseSoftware

class VisualStudioCode(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'VSCodeUserSetup-x64.exe'
        self.silent_install_args = ['/VERYSILENT', '/SUPPRESSMSGBOXES', '/NORESTART', '/SP-']

    def resolve_download_url(self):
        self.url_resolved.emit('https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user')
