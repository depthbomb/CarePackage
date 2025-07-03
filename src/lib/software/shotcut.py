from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class Shotcut(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('mltframework', 'shotcut', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'shotcut'
        self.name = 'Shotcut'
        self.category = [SoftwareCategory.Audio, SoftwareCategory.Media, SoftwareCategory.Utility]
        self.download_name = 'shotcut-win64.exe'
        self.should_cache_url = True
        self.icon = 'shotcut.png'
        self.homepage = 'https://shotcut.org'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if 'win64' in release and release.endswith('.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
