from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class HandBrake(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('HandBrake', 'HandBrake', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'handbrake'
        self.name = 'HandBrake'
        self.category = [SoftwareCategory.Media, SoftwareCategory.Utility]
        self.download_name = 'HandBrake-x86_64-Win_GUI.exe'
        self.should_cache_url = True
        self.icon = 'handbrake.png'
        self.homepage = 'https://handbrake.fr'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('-x86_64-Win_GUI.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
