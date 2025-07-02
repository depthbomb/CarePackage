from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class CaesiumImageCompressor(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('Lymphatus', 'caesium-image-compressor', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'caesium-image-compressor'
        self.name = 'Caesium Image Compressor'
        self.category = [SoftwareCategory.Utility]
        self.download_name = 'caesium-image-compressor-win-setup.exe'
        self.should_cache_url = True
        self.icon = 'caesium-image-compressor.png'
        self.homepage = 'https://saerasoft.com/caesium'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
