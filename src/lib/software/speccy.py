from re import compile
from PySide6.QtCore import QUrl, Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Speccy(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'speccy'
        self.name = 'Speccy'
        self.category = [SoftwareCategory.SystemManagement, SoftwareCategory.Utility]
        self.download_name = 'spsetup.exe'
        self.should_cache_url = True
        self.icon = 'speccy.png'
        self.homepage = 'https://www.ccleaner.com/speccy'

        self._download_page = QUrl('https://www.ccleaner.com/speccy/download/standard')

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        html = reply.readAll().data().decode()

        if reply.url() == self._download_page:
            module_page_pattern = compile(r'/en-us/api/modular-page\?guid=[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}')
            match = module_page_pattern.search(html)
            if not match:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            else:
                self.manager.get(QNetworkRequest(f'https://www.ccleaner.com{match.group(0)}'))
        else:
            download_url_pattern = compile(r'https://download\.ccleaner\.com/spsetup\d{2,3}\.exe')
            match = download_url_pattern.search(html)
            if not match:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            else:
                self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest(self._download_page))
