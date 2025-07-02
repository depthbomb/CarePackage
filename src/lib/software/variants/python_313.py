from src.lib.software import BaseSoftware
from PySide6.QtCore import Slot, QJsonDocument
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Python313(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'python-313'
        self.name = 'Python 3.13.x'
        self.download_name = 'python3.13.x-amd64.exe'
        self.should_cache_url = True
        self.icon = 'python.png'
        self.homepage = 'https://python.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        releases = QJsonDocument.fromJson(reply.readAll()).toVariant()
        candidates = [release for release in releases if release.get('is_latest') and release.get('version') == 3]
        if len(candidates) == 0:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        latest = candidates[0]
        version = str(latest.get('name', '')).split(' ')[1]

        self.url_resolved.emit(f'https://www.python.org/ftp/python/{version}/python-{version}-amd64.exe')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://python.org/api/v2/downloads/release'))
