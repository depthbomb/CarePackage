from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware
from src.lib.github_release_scraper import GithubReleaseScraper

class GodotCS(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('godotengine', 'godot', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'godot-cs'
        self.name = 'Godot (C# Support)'
        self.download_name = 'Godot-stable_mono_win64.zip'
        self.is_archive = True
        self.should_cache_url = True
        self.icon = 'godot.png'
        self.homepage = 'https://godotengine.org'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('-stable_mono_win64.zip')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
