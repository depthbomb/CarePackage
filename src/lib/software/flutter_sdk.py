from typing import cast
from PySide6.QtCore import QJsonDocument, Slot
from src.lib.software import BaseSoftware
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class FlutterSDK(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'flutter_windows_stable.zip'
        self.should_cache_url = True

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        json = QJsonDocument.fromJson(reply.readAll()).object()
        releases = cast(list, json.get('releases'))
        latest_release = releases[0]
        self.url_resolved.emit(f'https://storage.googleapis.com/flutter_infra_release/releases/{latest_release['archive']}')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://storage.googleapis.com/flutter_infra_release/releases/releases_windows.json'))
