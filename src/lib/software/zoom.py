from PySide6.QtCore import QJsonDocument, Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Zoom(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'zoom'
        self.name = 'Zoom Workplace'
        self.category = [SoftwareCategory.Social]
        self.download_name = 'ZoomInstallerFull.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.icon = 'zoom.png'
        self.homepage = 'https://zoom.us'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        text = reply.readAll().data()
        json = QJsonDocument.fromJson(text).object()
        zoomx64 = json['result']['downloadVO']['zoomX64']
        version = zoomx64['version']
        package_name = zoomx64['packageName']
        arch_type = zoomx64['archType']

        self.url_resolved.emit(f'https://zoom.us/client/{version}/{package_name}?archType={arch_type}')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://zoom.us/rest/download?os=win'))
