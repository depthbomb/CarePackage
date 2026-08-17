from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Blender(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'blender-windows-x64.msi'
        self.should_cache_url = True

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        html = reply.readAll().data().decode()

        pattern = compile(r'https://www\.blender\.org/download/release/(Blender\d+\.\d+/blender-\d\.\d+.\d+-windows-x64\.msi)')
        match = pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(f'https://mirrors.iu13.net/blender/release/{match.group(1)}')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.blender.org/download/'))
