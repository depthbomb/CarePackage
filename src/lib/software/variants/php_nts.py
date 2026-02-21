from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class PHPNTS(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'php-nts'
        self.name = 'PHP (Non Thread Safe)'
        self.download_name = 'php-nts-Win32-vs17-x64.zip'
        self.icon = 'php.png'
        self.is_archive = True
        self.homepage = 'https://php.net'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        html = reply.readAll().data().decode()
        pattern = compile(r'https://downloads\.php\.net/~windows/releases/archives/php-\d+\.\d+\.\d+-nts-Win32-vs17-x64\.zip')
        match = pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.php.net/downloads.php?usage=web&os=windows&osvariant=windows-downloads'))
