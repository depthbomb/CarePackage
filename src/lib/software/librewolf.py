from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class LibreWolf(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'librewolf'
        self.name = 'LibreWolf'
        self.category = [SoftwareCategory.Browser]
        self.download_name = 'librewolf-windows-x86_64-setup.exe'
        self.should_cache_url = True
        self.requires_admin = True
        self.icon = 'librewolf.png'
        self.homepage = 'https://librewolf.net'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'"(https://gitlab.com/api/v4/projects/\d{8}/packages/generic/librewolf/.*/librewolf-.*-windows-x86_64-setup\.exe)"')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(1))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://librewolf.net/installation/windows/'))
