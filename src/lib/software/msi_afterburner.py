from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.software.variants.msi_afterburner_beta import MSIAfterburnerBeta
from src.lib.software.variants.msi_afterburner_final import MSIAfterburnerFinal

class MSIAfterburner(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'msi-afterburner'
        self.name = 'MSI Afterburner'
        self.category = [SoftwareCategory.Peripheral, SoftwareCategory.SystemManagement]
        self.variants = [MSIAfterburnerFinal(), MSIAfterburnerBeta()]
        self.icon = 'msi-afterburner.png'
        self.homepage = 'https://msi.com/Landing/afterburner/graphics-cards'

    def resolve_download_url(self):
        pass
