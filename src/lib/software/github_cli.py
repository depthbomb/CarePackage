from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class GitHubCli(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'github-cli'
        self.name = 'GitHub CLI'
        self.category = SoftwareCategory.Development
        self.download_name = 'gh_windows_amd64.msi'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'github.png'
        self.homepage = 'https://cli.github.com'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://github.com/cli/cli/releases/download/v.*/gh_.*_windows_amd64\.msi')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://cli.github.com'))
