from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class ABDownloadManager(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('amir1376', 'ab-download-manager', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'abdownloadmanager'
        self.name = 'AB Download Manager'
        self.category = [SoftwareCategory.FileManagement]
        self.download_name = 'ABDownloadManager_windows_x64.exe'
        self.should_cache_url = True
        self.icon = 'abdownloadmanager.png'
        self.homepage = 'https://abdownloadmanager.com/'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
