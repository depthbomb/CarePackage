from src.lib.software import BaseSoftware

class UnityHub(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'UnityHubSetup-x64.exe'
        self.silent_install_args = ['/S']

    def resolve_download_url(self):
        self.url_resolved.emit('https://public-cdn.cloud.unity3d.com/hub/prod/UnityHubSetup-x64.exe')
