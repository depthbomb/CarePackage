from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Snes9X(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'snes9x'
        self.name = 'Snes9X'
        self.category = [SoftwareCategory.Emulation, SoftwareCategory.Gaming]
        self.download_name = 'snes9x-win32-x64.zip'
        self.is_archive = True
        self.should_cache_url = True
        self.icon = 'snes9x.png'
        self.homepage = 'https://snes9x.com'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        html = reply.readAll().data().decode()

        pattern = compile(r'https://dl\.emulator-zone\.com/download\.php/emulators/snes/snes9x/snes9x-\d+\.\d+\.\d+-win32-x64\.zip')
        match = pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.emulator-zone.com/snes/snes9x'))
