from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class SevenZip(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('ip7z', '7zip', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'seven-zip'
        self.name = '7-Zip'
        self.category = SoftwareCategory.Utility
        self.download_name = '7zSetup.msi'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = '7zip.png'
        self.homepage = 'https://7-zip.org'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('-x64.msi')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
