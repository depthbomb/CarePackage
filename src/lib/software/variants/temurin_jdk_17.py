from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware
from src.lib.github_release_scraper import GithubReleaseScraper

class TemurinJDK17(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('adoptium', 'temurin17-binaries', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'temurin-jdk-17'
        self.name = 'Temurin JDK 17 - LTS'
        self.download_name = 'OpenJDK17U-jdk_x64_windows_hotspot.msi'
        self.is_archive = False
        self.should_cache_url = True
        self.icon = 'temurin.png'
        self.homepage = 'https://adoptium.net'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if 'x64_windows_hotspot' in release and release.endswith('.msi')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
