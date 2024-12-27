from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class Godot(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('godotengine', 'godot', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'godot'
        self.name = 'Godot'
        self.category = SoftwareCategory.Creative
        self.download_name = 'Godot-stable_win64.exe.zip'
        self.is_archive = True
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'godot.png'
        self.homepage = 'https://godotengine.org'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('-stable_win64.exe.zip')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
