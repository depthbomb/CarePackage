from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Signal(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'signal-desktop'
        self.name = 'Signal'
        self.category = [SoftwareCategory.Social]
        self.download_name = 'signal-desktop-win.exe'
        self.should_cache_url = True
        self.icon = 'signal.png'
        self.homepage = 'https://signal.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'signal-desktop-win-\d+\.\d+\.\d+\.exe')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(f'https://updates.signal.org/desktop/{match.group(0)}')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://updates.signal.org/desktop/latest.yml'))
