from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class PaintDotNet(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('paintdotnet', 'release', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'paint-dot-net'
        self.name = 'Paint.NET'
        self.category = SoftwareCategory.Creative
        self.download_name = 'Paint.NET.zip'
        self.is_archive = True
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'paintdotnet.png'
        self.homepage = 'https://getpaint.net'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('.install.x64.zip')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
