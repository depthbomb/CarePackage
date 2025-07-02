from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class Yay(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('depthbomb', 'yay', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'yay'
        self.name = 'yay'
        self.category = [SoftwareCategory.Media, SoftwareCategory.Utility]
        self.download_name = 'yay-setup.exe'
        self.should_cache_url = True
        self.icon = 'yay.png'
        self.homepage = 'https://github.com/depthbomb/yay'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
