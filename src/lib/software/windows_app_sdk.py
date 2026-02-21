from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class WindowsAppSdk(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'windows-app-sdk'
        self.name = 'Windows App SDK'
        self.category = [SoftwareCategory.Development, SoftwareCategory.Runtime]
        self.download_name = 'WindowsAppRuntimeInstall-x64.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.icon = 'generic.png'
        self.homepage = 'https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        pattern = compile(r'https://aka\.ms/windowsappsdk/\d+\.\d+/\d+\.\d+\.\d+/windowsappruntimeinstall-x64.exe')
        html = reply.readAll().data().decode()
        match = pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/downloads'))
