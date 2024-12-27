from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class WinDirStat(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('windirstat', 'windirstat', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'windirstat'
        self.name = 'WinDirStat'
        self.category = SoftwareCategory.Utility
        self.download_name = 'WinDirStat-x64.msi'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'windirstat.png'
        self.homepage = 'https://windirstat.net'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('-x64.msi')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
