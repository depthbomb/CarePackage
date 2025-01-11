from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class HeroicGamesLauncher(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('Heroic-Games-Launcher', 'HeroicGamesLauncher', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'heroic-games-launcher'
        self.name = 'Heroic Games Launcher'
        self.category = SoftwareCategory.Gaming
        self.download_name = 'Heroic-Setup-x64.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'heroic-games-launcher.png'
        self.homepage = 'https://heroicgameslauncher.com'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('-Setup-x64.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
