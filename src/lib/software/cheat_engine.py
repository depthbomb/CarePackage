from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class CheatEngine(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'cheat-engine'
        self.name = 'Cheat Engine'
        self.category = [SoftwareCategory.Gaming, SoftwareCategory.Utility]
        self.download_name = 'CheatEngine.exe'
        self.should_cache_url = True
        self.icon = 'cheat-engine.png'
        self.homepage = 'https://cheatengine.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        html = reply.readAll().data().decode()

        pattern = compile(r'https://\w{13,}\.cloudfront\.net/installer/\d+/\d+')
        match = pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://cheatengine.org/downloads.php'))
