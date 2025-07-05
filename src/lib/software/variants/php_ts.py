from re import compile
from src import USER_AGENT
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class PHPTS(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'php-ts'
        self.name = 'PHP (Thread Safe)'
        self.download_name = 'php-Win32-vs17-x64.zip'
        self.icon = 'php.png'
        self.is_archive = True
        self.homepage = 'https://php.net'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        print(reply.readAll().data().decode())
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        pattern = compile(r'\"PHP (\d\.\d+\.\d+)\",')
        text = reply.readAll().data().decode()
        match = pattern.search(text)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            version = match.group(1)
            self.url_resolved.emit(f'https://windows.php.net/downloads/releases/php-{version}-Win32-vs17-x64.zip')

    def resolve_download_url(self):
        req = QNetworkRequest('https://api.github.com/repos/php/php-src/releases/latest')
        req.setRawHeader(b'user-agent', USER_AGENT.encode())
        self.manager.get(req)
