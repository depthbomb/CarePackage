from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class ApacheNetBeans(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('codelerity', 'netbeans-installers', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'apache-netbeans'
        self.name = 'Apache NetBeans'
        self.category = [SoftwareCategory.Development]
        self.download_name = 'Apache-NetBeans-bin-windows-x64.exe'
        self.should_cache_url = True
        self.requires_admin = True
        self.icon = 'apache-netbeans.png'
        self.homepage = 'https://netbeans.apache.org'

        self._current_ver = 30

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
