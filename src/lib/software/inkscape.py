from re import compile
from PySide6.QtCore import Slot, QUrl
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Inkscape(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'inkscape'
        self.name = 'Inkscape'
        self.category = SoftwareCategory.Creative
        self.download_name = 'inkscape-x64.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = True
        self.icon = 'inkscape.png'
        self.homepage = 'https://inkscape.org'

        self._first_request = True
        self._initial_url = QUrl('https://inkscape.org/release/')

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        if self._first_request:
            self._first_request = False
            url = reply.url().toString()
            url += 'windows/64-bit/exe/dl'
            self.manager.get(QNetworkRequest(url))
        else:
            download_url_pattern = compile(r'"(/gallery/item/\d{5,}/inkscape-.*-x64\.exe)"')
            html = reply.readAll().data().decode()
            match = download_url_pattern.search(html)
            if not match:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            else:
                self.url_resolved.emit(f'https://inkscape.org{match.group(1)}')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest(self._initial_url))
