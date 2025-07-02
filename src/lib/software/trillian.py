from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Trillian(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'trillian'
        self.name = 'Trillian'
        self.category = [SoftwareCategory.Social]
        self.download_name = 'trillian.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.icon = 'trillian.png'
        self.homepage = 'https://trillian.im'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        pattern = compile(r'<a href="(/get/windows/.*/)">Try downloading again\.</a>')
        html = reply.readAll().data().decode()
        match = pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(f'{self.homepage}{match.group(1)}')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://trillian.im/get/windows/thanks/'))
