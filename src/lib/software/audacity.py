from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class Audacity(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('audacity', 'audacity', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'audacity'
        self.name = 'Audacity'
        self.category = SoftwareCategory.Media
        self.download_name = 'audacity-win-64bit.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'audacity.png'
        self.homepage = 'https://audacityteam.org'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('-64bit.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.error_occurred.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
