from src.lib.software import BaseSoftware, SoftwareCategory

class BattleNet(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'blizzard-battle-net'
        self.name = 'Battle.net'
        self.category = [SoftwareCategory.Gaming]
        self.download_name = 'Battle.net-Setup.exe'
        self.icon = 'battlenet.png'
        self.homepage = 'https://battle.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://downloader.battle.net/download/getInstallerForGame?os=win&gameProgram=BATTLENET_APP&version=Live')
