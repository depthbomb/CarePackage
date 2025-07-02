from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class NotepadPlusPlus(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('notepad-plus-plus', 'notepad-plus-plus', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'notepad-plus-plus'
        self.name = 'Notepad++'
        self.category = [SoftwareCategory.Development]
        self.download_name = 'npp.Installer.x64.exe'
        self.should_cache_url = True
        self.requires_admin = True
        self.icon = 'notepad-plus-plus.png'
        self.homepage = 'https://notepad-plus-plus.org'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('.Installer.x64.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
