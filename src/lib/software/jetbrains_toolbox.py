from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class JetBrainsToolbox(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'jetbrains-toolbox'
        self.name = 'JetBrains Toolbox'
        self.category = [SoftwareCategory.Development]
        self.download_name = 'jetbrains-toolbox.exe'
        self.should_cache_url = True
        self.icon = 'jetbrains-toolbox.png'
        self.homepage = 'https://jetbrains.com/toolbox-app'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://download\.jetbrains\.com/toolbox/jetbrains-toolbox-\d+\.\d+\.\d+\.\d+\.exe\b')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://data.services.jetbrains.com/products/releases?code=TBA&latest=true&type=release'))
