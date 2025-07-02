from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class MinGW(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'mingw'
        self.name = 'MinGW'
        self.category = [SoftwareCategory.Development]
        self.download_name = 'mingw-get-setup.exe'
        self.should_cache_url = True
        self.icon = 'mingw.png'
        self.homepage = 'https://sourceforge.net/projects/mingw'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'<a href="(.*)" rel="nofollow">')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(1))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://sourceforge.net/settings/mirror_choices?projectname=mingw&filename=Installer/mingw-get-setup.exe&dialog=true'))
