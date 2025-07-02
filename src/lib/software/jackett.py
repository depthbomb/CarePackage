from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class Jackett(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('Jackett', 'Jackett', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'jackett'
        self.name = 'Jackett'
        self.category = [SoftwareCategory.FileManagement, SoftwareCategory.Utility]
        self.download_name = 'Jackett.Installer.Windows.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.icon = 'jackett.png'
        self.homepage = 'https://github.com/Jackett/Jackett'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('Jackett.Installer.Windows.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
