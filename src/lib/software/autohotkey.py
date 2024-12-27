from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class AutoHotkey(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('AutoHotkey', 'AutoHotkey', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'autohotkey'
        self.name = 'AutoHotkey'
        self.category = SoftwareCategory.Utility
        self.download_name = 'AutoHotkey_setup.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'autohotkey.png'
        self.homepage = 'https://autohotkey.com'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('_setup.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
