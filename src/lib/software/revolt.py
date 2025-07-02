from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class Revolt(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('revoltchat', 'desktop', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'revolt'
        self.name = 'Revolt'
        self.category = [SoftwareCategory.Social]
        self.download_name = 'Revolt-Setup.exe'
        self.should_cache_url = True
        self.icon = 'revolt.png'
        self.homepage = 'https://revolt.chat'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
