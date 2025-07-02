from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class ShadPS4(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('shadps4-emu', 'shadPS4', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'shadps4'
        self.name = 'ShadPS4'
        self.category = [SoftwareCategory.Emulation, SoftwareCategory.Gaming]
        self.download_name = 'shadps4-win64-qt.zip'
        self.is_archive = True
        self.should_cache_url = True
        self.icon = 'shadps4.png'
        self.homepage = 'https://shadps4.net'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if 'shadps4-win64-qt' in release), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
