from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class CMake(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('Kitware', 'CMake', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'cmake'
        self.name = 'CMake'
        self.category = SoftwareCategory.Development
        self.download_name = 'cmake-windows-x86_64.msi'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'cmake.png'
        self.homepage = 'https://cmake.org'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('-windows-x86_64.msi')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
