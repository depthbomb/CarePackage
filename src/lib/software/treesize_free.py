from src.lib.software import BaseSoftware, SoftwareCategory

class TreeSizeFree(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'treesize-free'
        self.name = 'TreeSize Free'
        self.category = [SoftwareCategory.FileManagement, SoftwareCategory.SystemManagement, SoftwareCategory.Utility]
        self.download_name = 'TreeSizeFreeSetup.exe'
        self.icon = 'treesize.png'
        self.homepage = 'https://jam-software.com/treesize_free'

    def resolve_download_url(self):
        self.url_resolved.emit('https://downloads.jam-software.de/treesize_free/TreeSizeFreeSetup.exe')
