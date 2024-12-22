from json import dumps
from re import compile, RegexFlag
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest
from PySide6.QtCore import Slot, QUrl, QByteArray, QJsonDocument

class QBitTorrent(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'qbittorrent'
        self.name = 'qBittorrent'
        self.category = SoftwareCategory.Utility
        self.download_name = 'qbittorrent_x64_setup.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'qbittorrent.png'
        self.homepage = 'https://qbittorrent.org'

        self._initial_url = QUrl('https://www.fosshub.com/qBittorrent.html')

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        text = reply.readAll()

        if reply.url() == self._initial_url:
            settings_pattern = compile(r'<script>\s+var settings =(.*)\s+</script>', RegexFlag.MULTILINE)
            match = settings_pattern.search(text.toStdString())
            if not match:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            else:
                json = QJsonDocument.fromJson(match.group(1).encode()).object()
                project_id = json['projectId']
                project_uri = json['pool']['u']
                project_files = json['pool']['f']

                latest_release = project_files[0]
                latest_file = latest_release['n']
                latest_id = latest_release['r']

                payload_json = dumps({
                    'projectId': project_id,
                    'releaseId': latest_id,
                    'projectUri': project_uri,
                    'fileName': latest_file,
                    'source': 'CF',
                })

                req = QNetworkRequest('https://api.fosshub.com/download/')
                req.setHeader(QNetworkRequest.KnownHeaders.ContentTypeHeader, 'application/json')

                self.manager.post(req, QByteArray(payload_json.encode()))
        else:
            json = QJsonDocument.fromJson(text).object()
            self.url_resolved.emit(json['data']['url'])

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest(self._initial_url))
