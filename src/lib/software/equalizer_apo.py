from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class EqualizerApo(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'equalizer-apo'
        self.name = 'Equalizer APO'
        self.category = [SoftwareCategory.Audio, SoftwareCategory.Utility]
        self.download_name = 'EqualizerAPO-x64.exe'
        self.icon = 'equalizer-apo.png'
        self.homepage = 'https://sourceforge.net/projects/equalizerapo'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        self.url_resolved.emit(reply.url().toString())

    def resolve_download_url(self):
        req = QNetworkRequest('https://sourceforge.net/projects/equalizerapo/files/latest/download')
        req.setRawHeader(b'user-agent', b'Wget/1.20.3')

        self.manager.get(req)
