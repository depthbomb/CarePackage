from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class VisualStudioCommunity(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'visual-studio-community'
        self.name = 'Visual Studio 2022 Community'
        self.category = SoftwareCategory.Development
        self.download_name = 'VisualStudioSetup.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'visual-studio-community.png'
        self.homepage = 'https://visualstudio.microsoft.com'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://c2rsetup\.officeapps\.live\.com/c2r/downloadVS\.aspx\?sku=community&channel=Release&version=VS\d{4}&passive=true')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&channel=Release'))
