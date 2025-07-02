from src.lib.software import BaseSoftware

class MSIAfterburnerBeta(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'msi-afterburner-beta'
        self.name = 'MSI Afterburner Beta'
        self.download_name = 'MSIAfterburnerInstallerBeta.zip'
        self.is_archive = True
        self.icon = 'msi-afterburner.png'
        self.homepage = 'https://www.msi.com/Landing/afterburner/graphics-cards'

        self._initial_request = True

    def resolve_download_url(self):
        self.url_resolved.emit('https://ftp.nluug.nl/pub/games/PC/guru3d/afterburner/[Guru3D]-MSIAfterburnerSetup466Beta5Build16555.zip')
