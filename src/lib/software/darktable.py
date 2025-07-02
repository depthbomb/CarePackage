from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class Darktable(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('darktable-org', 'darktable', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'darktable'
        self.name = 'darktable'
        self.category = [SoftwareCategory.Creative, SoftwareCategory.Media]
        self.download_name = 'darktable-win64.exe'
        self.should_cache_url = True
        self.requires_admin = True
        self.icon = 'darktable.png'
        self.homepage = 'https://darktable.org'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('win64.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
