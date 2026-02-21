from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Thunderbird(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'thunderbird'
        self.name = 'Thunderbird'
        self.category = [SoftwareCategory.Productivity, SoftwareCategory.Social]
        self.download_name = 'Thunderbird_Setup.exe'
        self.should_cache_url = True
        self.icon = 'thunderbird.png'
        self.homepage = 'https://thunderbird.net'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://download\.mozilla\.org/\?product=thunderbird-(.*)-SSL&os=win64&lang=en-US')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.thunderbird.net/en-US/download/'))
