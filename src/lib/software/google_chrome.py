from re import compile
from uuid import uuid4
from PySide6.QtCore import Slot, QUrl
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class GoogleChrome(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'google-chrome'
        self.name = 'Google Chrome'
        self.category = SoftwareCategory.Browser
        self.download_name = 'ChromeSetup.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'google-chrome.png'
        self.homepage = 'https://google.com/chrome'

        self._initial_url = QUrl('https://www.google.com/chrome/static/js/installer.min.js')

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        app_guid_pattern = compile(r'stablechannel:"(?P<guid>[{(]?[0-9A-F]{8}-?(?:[0-9A-F]{4}-?){3}[0-9A-F]{12}[)}]?)"')
        text = reply.readAll().data().decode()
        match = app_guid_pattern.search(text)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            iid = '{' + str(uuid4()) + '}'
            app_guid = match.group('guid')
            path = QUrl.toPercentEncoding(f'appguid={app_guid}&iid={iid}&lang=en&browser=4&usagestats=0&appname=Google%20Chrome&needsadmin=prefers&ap=x64-statsdef_1&').data().decode()
            download_url = f'https://dl.google.com/tag/s/{path}installdataindex=empty/update2/installers/ChromeSetup.exe'
            self.url_resolved.emit(download_url)

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest(self._initial_url))
