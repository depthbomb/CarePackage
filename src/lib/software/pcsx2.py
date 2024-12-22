from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class PCSX2(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('pcsx2', 'pcsx2', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'pcsx2-stable'
        self.name = 'PCSX2'
        self.category = SoftwareCategory.Gaming
        self.download_name = 'PCSX2.7z'
        self.is_archive = True
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'pcsx2.png'
        self.homepage = 'https://pcsx2.net'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('windows-x64-Qt.7z')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
