from re import compile
from PySide6.QtCore import Slot, QUrl
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class KeePass(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'keepass'
        self.name = 'KeePass'
        self.category = [SoftwareCategory.Security]
        self.download_name = 'KeePass-Setup.exe'
        self.icon = 'keepass.png'
        self.homepage = 'https://keepass.info'

        self._initial_url = QUrl('https://keepass.info/download.html')

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        html = reply.readAll().data().decode()

        if reply.url() == self._initial_url:
            download_file_name_pattern = compile(r'https://sourceforge\.net/projects/keepass/files/(KeePass%202\.x/\d+\.\d+(\.\d+)?/KeePass-\d+\.\d+(\.\d+)?-Setup\.exe)/download')
            match = download_file_name_pattern.search(html)
            if not match:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            else:
                req = QNetworkRequest(f'https://sourceforge.net/settings/mirror_choices?projectname=keepass&filename={match.group(1)}&dialog=true')
                self.manager.get(req)
        else:
            download_url_pattern = compile(r'<a href="(.*)" rel="nofollow">')
            match = download_url_pattern.search(html)
            if not match:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            else:
                self.url_resolved.emit(match.group(1))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest(self._initial_url))
