from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.github_release_scraper import GithubReleaseScraper

class GitForWindows(BaseSoftware):
    def __init__(self):
        super().__init__()

        self._gh = GithubReleaseScraper('git-for-windows', 'git', self)
        self._gh.releases_scraped.connect(self._on_releases_scraped)

        self.key = 'git-for-windows'
        self.name = 'Git for Windows'
        self.category = SoftwareCategory.Development
        self.download_name = 'Git-64-bit.exe'

        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'git.png'
        self.homepage = 'https://git-scm.com'

    @Slot(list)
    def _on_releases_scraped(self, releases: list[str]):
        asset = next((release for release in releases if 'Git-' in release and release.endswith('-64-bit.exe')), None)
        if asset:
            self.url_resolved.emit(asset)
        else:
            self.url_resolve_error.emit(self.ResolveError.GitHubAssetNotFoundError)

    def resolve_download_url(self):
        self._gh.get_repo_releases()
