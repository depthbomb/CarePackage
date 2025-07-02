from src.lib.software.variants.plexamp import Plexamp
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.software.variants.plex_desktop import PlexDesktop
from src.lib.software.variants.plex_media_server import PlexMediaServer

class Plex(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'plex'
        self.name = 'Plex'
        self.category = [SoftwareCategory.Audio, SoftwareCategory.Media]
        self.variants = [PlexDesktop(), Plexamp(), PlexMediaServer()]
        self.icon = 'plex-desktop.png'
        self.homepage = 'https://plex.tv'

    def resolve_download_url(self):
        pass
