from src.lib.software import BaseSoftware, SoftwareCategory

class Msvc(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'msvc-140-170'
        self.name = 'Microsoft Visual C++ 2015-2022 Redistributable'
        self.category = [SoftwareCategory.Runtime]
        self.download_name = 'VC_redist.x64.exe'
        self.icon = 'msvc.png'
        self.homepage = 'https://learn.microsoft.com/en-us/cpp/windows/latest-supported-vc-redist?view=msvc-170'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.visualstudio.microsoft.com/download/pr/c7dac50a-e3e8-40f6-bbb2-9cc4e3dfcabe/1821577409C35B2B9505AC833E246376CC68A8262972100444010B57226F0940/VC_redist.x64.exe')
