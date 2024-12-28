from src.lib.software import BaseSoftware, SoftwareCategory

class AdobeCreativeCloud(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'adobe-creative-cloud'
        self.name = 'Adobe Creative Cloud'
        self.category = SoftwareCategory.Creative
        self.download_name = 'Creative_Cloud_Set-Up.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'adobe-creative-cloud.png'
        self.homepage = 'https://www.adobe.com/creativecloud.html'

    def resolve_download_url(self):
        self.url_resolved.emit('https://prod-rel-ffc-ccm.oobesaas.adobe.com/adobe-ffc-external/core/v1/wam/download?sapCode=KCCC&productName=Creative%20Cloud&os=win&guid=5bc31f02-fa9a-4004-b27a-1f6d959c2c45&environment=prod&api_key=CCHomeWeb1')
