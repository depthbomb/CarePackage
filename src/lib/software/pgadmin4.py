from re import compile
from PySide6.QtCore import Slot
from packaging.version import Version
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class PgAdmin4(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'pgadmin4'
        self.name = 'pgAdmin 4'
        self.category = [SoftwareCategory.Development, SoftwareCategory.Utility]
        self.download_name = 'pgadmin4-x64.exe'
        self.icon = 'pgadmin4.png'
        self.homepage = 'https://pgadmin.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()

        if reply.error() != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        html = reply.readAll().data().decode()
        pattern = compile(r'href="v(\d+(?:\.\d+)*)/index\.html"')
        versions = pattern.findall(html)
        if not versions:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        version = str(max(Version(v) for v in versions))

        self.url_resolved.emit(f'https://pgadmin-archive.postgresql.org/pgadmin4/v{version}/windows/pgadmin4-{version}-x64.exe')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://pgadmin-archive.postgresql.org/pgadmin4/index.html'))
