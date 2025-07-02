from src.lib.software import BaseSoftware, SoftwareCategory

class DisplayDriverUninstaller(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'display-driver-uninstaller'
        self.name = 'Display Driver Uninstaller'
        self.category = [SoftwareCategory.Utility]
        self.download_name = '[Guru3D.com]-DDU.zip'
        self.is_archive = True
        self.icon = 'ddu.png'
        self.homepage = 'https://guru3d.com/download/display-driver-uninstaller-download'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download-eu2.guru3d.com/ddu/[Guru3D]-DDU.zip')
