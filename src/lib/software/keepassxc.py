from PySide6.QtCore import Slot, QUrl
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class KeePassXC(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('keepassxreboot', 'keepassxc', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'keepassxc'
        self.name = 'KeePassXC'
        self.category = [SoftwareCategory.Security, SoftwareCategory.Utility]
        self.download_name = 'KeePassXC-Win64.msi'
        self.should_cache_url = True
        self.icon = 'keepassxc.png'
        self.homepage = 'https://keepassxc.org'

        self._initial_url = QUrl('https://keepass.info/download.html')

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('Win64.msi')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
