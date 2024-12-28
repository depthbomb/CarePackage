from re import compile
from PySide6.QtCore import Slot
from packaging.version import Version
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class NodeJsLts(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'nodejs-lts'
        self.name = 'Node.js (LTS)'
        self.category = SoftwareCategory.Development
        self.download_name = 'node-lts-x64.msi'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'nodejs.png'
        self.homepage = 'https://nodejs.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        version_pattern = compile(r'dist/(v\d{2}\.\d{1,2}\.\d+)/node')
        html = reply.readAll().data().decode()
        matches = version_pattern.finditer(html)
        versions = []
        for match in matches:
            ver = match.group(1)
            versions.append(ver)

        if len(versions) == 0:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            latest_version = min(versions, key=lambda x: Version(x))
            self.url_resolved.emit(f'https://nodejs.org/dist/{latest_version}/node-{latest_version}-x64.msi')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://nodejs.org/en'))
