from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class Azahar(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('azahar-emu', 'azahar', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'azahar'
        self.name = 'Azahar'
        self.category = [SoftwareCategory.Emulation, SoftwareCategory.Gaming]
        self.download_name = 'azahar-windows-msys2-installer.exe'
        self.should_cache_url = True
        self.icon = 'azahar.png'
        self.homepage = 'https://azahar-emu.org'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('-windows-msys2-installer.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
