from src.lib.software import BaseSoftware

class MSIAfterburnerFinal(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'msi-afterburner-final'
        self.name = 'MSI Afterburner Final'
        self.download_name = 'MSIAfterburnerSetup.zip'
        self.is_archive = True
        self.icon = 'msi-afterburner.png'
        self.homepage = 'https://www.msi.com/Landing/afterburner/graphics-cards'

    def resolve_download_url(self):
        self.url_resolved.emit('https://ftp.nluug.nl/pub/games/PC/guru3d/afterburner/[Guru3D.com]-MSIAfterburnerSetup465.zip')
