from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class Streamlink(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('streamlink', 'windows-builds', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'streamlink'
        self.name = 'Streamlink'
        self.category = [SoftwareCategory.Media]
        self.download_name = 'streamlink-x86_64.exe'
        self.should_cache_url = True
        self.requires_admin = True
        self.icon = 'streamlink.png'
        self.homepage = 'https://streamlink.github.io'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset_pattern = compile(r'streamlink-\d+\.\d+\.\d+(?:-\d+)?-py3\d+-x86_64\.exe')
        asset = next((release for release in releases if asset_pattern.search(release)), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
