from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware
from src.lib.github_release_scraper import GithubReleaseScraper

class Azahar(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('azahar-emu', 'azahar', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.download_name = 'azahar-windows-msvc-installer.exe'
        self.silent_install_args = ['/S']
        self.should_cache_url = True

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if 'msvc-' in release and release.endswith('-installer.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
