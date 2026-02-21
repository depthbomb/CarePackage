from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class MPV(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('mpv-player', 'mpv', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'mpv'
        self.name = 'mpv'
        self.category = [SoftwareCategory.Audio, SoftwareCategory.Media]
        self.download_name = 'mpv-x86_64-pc-windows-msvc.zip'
        self.is_archive = True
        self.icon = 'mpv.png'
        self.homepage = 'https://mpv.io'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('x86_64-pc-windows-msvc.zip')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
