from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware
from src.lib.github_release_scraper import GithubReleaseScraper

class DnSpy(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('dnSpyEx', 'dnSpy', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.download_name = 'dnSpy-net-win64.zip'
        self.should_cache_url = True

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('win64.zip')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
