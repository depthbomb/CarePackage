from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware
from src.lib.github_release_scraper import GithubReleaseScraper

class DuckStation(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('stenzek', 'duckstation', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.download_name = 'duckstation-windows-x64-installer.exe'
        self.should_cache_url = True

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if 'duckstation-windows-x64-installer.exe' in release), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
