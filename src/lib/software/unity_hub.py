from src.lib.software import BaseSoftware, SoftwareCategory

class UnityHub(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'unity-hub'
        self.name = 'Unity Hub'
        self.category = SoftwareCategory.Creative
        self.download_name = 'UnityHubSetup.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = True
        self.icon = 'unity-hub.png'
        self.homepage = 'https://unity.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://public-cdn.cloud.unity3d.com/hub/prod/UnityHubSetup.exe')
