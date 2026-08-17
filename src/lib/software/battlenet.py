from src.lib.software import BaseSoftware

class BattleNet(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'Battle.net-Setup.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://downloader.battle.net/download/getInstallerForGame?os=win&gameProgram=BATTLENET_APP&version=Live')
