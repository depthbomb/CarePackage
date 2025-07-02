from re import compile
from PySide6.QtCore import Slot, QUrl
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class NSIS(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'nsis'
        self.name = 'NSIS'
        self.category = [SoftwareCategory.Development]
        self.download_name = 'nsis-setup.exe'
        self.should_cache_url = True
        self.requires_admin = True
        self.icon = 'nsis.png'
        self.homepage = 'https://nsis.sourceforge.io'

        self._major_version = 3  # Update this if version 4 is ever a thing
        self._initial_url = QUrl('https://nsis.sourceforge.io/Download')

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        html = reply.readAll().data().decode()

        if reply.url() == self._initial_url:
            version_pattern = compile(r'https://prdownloads\.sourceforge\.net/nsis/nsis-(\d+\.\d+)-setup\.exe\?download')
            match = version_pattern.search(html)
            if not match:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            else:
                version = match.group(1)
                req = QNetworkRequest(f'https://sourceforge.net/settings/mirror_choices?projectname=nsis&filename=NSIS%20{self._major_version}/{version}/nsis-{version}-setup.exe&dialog=true')
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
