from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class ShadPS4(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'shadps4-win64-qt.zip'
        self.should_cache_url = True

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        json = reply.readAll().data().decode()

        pattern = compile(r'https://github\.com/shadps4-emu/shadps4-qtlauncher/releases/download/shadPS4QtLauncher-\d+-\d+-\d+-[a-f0-9]{40}/shadPS4QtLauncher-win64-qt-\d+-\d+-\d+-[a-f0-9]{7}\.zip')
        match = pattern.search(json)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://api.github.com/repos/shadps4-emu/shadps4-qtlauncher/releases'))
