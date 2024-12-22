from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class PowerToys(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('microsoft', 'PowerToys', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'microsoft-powertoys'
        self.name = 'PowerToys'
        self.category = SoftwareCategory.Utility
        self.download_name = 'PowerToysUserSetup-x64.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'powertoys.png'
        self.homepage = 'https://learn.microsoft.com/en-us/windows/powertoys'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if 'PowerToysSetup-' in release and release.endswith('-x64.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
