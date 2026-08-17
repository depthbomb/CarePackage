from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware
from src.lib.github_release_scraper import GithubReleaseScraper

class Rufus(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('pbatard', 'rufus', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.download_name = 'rufus.exe'
        self.should_cache_url = True

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        release_pattern = compile(r'rufus-\d+\.\d+\.exe')
        asset = next((release for release in releases if release_pattern.search(release)), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
