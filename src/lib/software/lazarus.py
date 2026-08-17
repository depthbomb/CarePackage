from re import compile
from PySide6.QtCore import Slot, QUrl
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Lazarus(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'lazarus'
        self.name = 'Lazarus'
        self.category = [SoftwareCategory.Development]
        self.download_name = 'lazarus-fpc-win64.exe'
        self.icon = 'lazarus.png'
        self.homepage = 'https://lazarus-ide.org'

        self._initial_url = QUrl('https://download.lazarus-ide.org/Lazarus%20Windows%2064%20bits/')

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        html = reply.readAll().data().decode()

        if reply.url() == self._initial_url:
            release_directory_pattern = compile(r'href="(Lazarus%20(\d+(?:\.\d+)*)/)"')
            release_directories = release_directory_pattern.findall(html)
            if not release_directories:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            else:
                latest_directory = max(
                    release_directories,
                    key=lambda release: tuple(map(int, release[1].split('.')))
                )[0]
                release_url = self._initial_url.resolved(QUrl(latest_directory))
                self.manager.get(QNetworkRequest(release_url))
        else:
            download_url_pattern = compile(
                r'href="(lazarus-\d+(?:\.\d+)*-fpc-\d+(?:\.\d+)*-win64\.exe)"'
            )
            match = download_url_pattern.search(html)
            if not match:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            else:
                download_url = reply.url().resolved(QUrl(match.group(1)))
                self.url_resolved.emit(download_url.toEncoded().data().decode())

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest(self._initial_url))
