from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class RPCS3(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('RPCS3', 'rpcs3-binaries-win', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'rpcs3'
        self.name = 'RPCS3'
        self.category = [SoftwareCategory.Emulation, SoftwareCategory.Gaming]
        self.download_name = 'rpcs3-win64_msvc.7z'
        self.is_archive = True
        self.should_cache_url = True
        self.icon = 'rpcs3.png'
        self.homepage = 'https://rpcs3.net'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('.7z')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
