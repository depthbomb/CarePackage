from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class DBBrowserForSQLite(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('sqlitebrowser', 'sqlitebrowser', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'db-browser-for-sqlite'
        self.name = 'DB Browser for SQLite'
        self.category = [SoftwareCategory.Development, SoftwareCategory.Utility]
        self.download_name = 'DB.Browser.for.SQLite-win64.msi'
        self.should_cache_url = True
        self.icon = 'db-browser-for-sqlite.png'
        self.homepage = 'https://sqlitebrowser.org'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if release.endswith('-win64.msi')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
