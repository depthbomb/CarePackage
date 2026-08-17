from uuid import uuid4
from src.lib.software import BaseSoftware

class AdobeCreativeCloud(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'Creative_Cloud_Set-Up.exe'

    def resolve_download_url(self):
        self.url_resolved.emit(f'https://prod-rel-ffc-ccm.oobesaas.adobe.com/adobe-ffc-external/core/v1/wam/download?sapCode=KCCC&productName=Creative%20Cloud&os=win&guid={uuid4()}&environment=prod&api_key=CCHomeWeb1')
