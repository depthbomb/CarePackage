from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class VeraCrypt(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('veracrypt', 'VeraCrypt', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'veracrypt'
        self.name = 'VeraCrypt'
        self.category = [SoftwareCategory.Security, SoftwareCategory.SystemManagement]
        self.download_name = 'VeraCrypt.Setup.exe'
        self.should_cache_url = True
        self.icon = 'veracrypt.png'
        self.homepage = 'https://veracrypt.io'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if '.Setup.' in release and release.endswith('.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
