from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class Obsidian(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('obsidianmd', 'obsidian-releases', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'obsidian'
        self.name = 'Obsidian'
        self.category = SoftwareCategory.Development
        self.download_name = 'Obsidian.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'obsidian.png'
        self.homepage = 'https://obsidian.md'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
