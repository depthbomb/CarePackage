from src.lib.software import BaseSoftware

class TreeSizeFree(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'TreeSizeFreeSetup.exe'
        self.silent_install_args = ['/VERYSILENT', '/SUPPRESSMSGBOXES', '/NORESTART', '/SP-']

    def resolve_download_url(self):
        self.url_resolved.emit('https://downloads.jam-software.de/treesize_free/TreeSizeFreeSetup.exe')
