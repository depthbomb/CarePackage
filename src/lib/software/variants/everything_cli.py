from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware
from src.lib.github_release_scraper import GithubReleaseScraper

class EverythingCLI(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('voidtools', 'ES', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'everything-cli'
        self.name = 'Everything Command Line Interface'
        self.download_name = 'ES.x64.zip'
        self.should_cache_url = True
        self.is_cli = True
        self.icon = 'generic.png'
        self.homepage = 'https://github.com/voidtools/ES'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('.x64.zip')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
