from src.lib.software import BaseSoftware, SoftwareCategory

class MPV(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'mpv'
        self.name = 'mpv'
        self.category = [SoftwareCategory.Audio, SoftwareCategory.Media]
        self.download_name = 'mpv-x86_64-pc-windows-msvc.zip'
        self.is_archive = True
        self.icon = 'mpv.png'
        self.homepage = 'https://mpv.io'

    def resolve_download_url(self):
        self.url_resolved.emit('https://nightly.link/mpv-player/mpv/workflows/build/master/mpv-x86_64-pc-windows-msvc.zip')
