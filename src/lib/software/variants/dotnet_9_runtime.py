from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class DotNet9Runtime(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'dotnet-9-runtime'
        self.name = '.NET 9.0 Runtime'
        self.download_name = 'dotnet-runtime-9.0-win-x64.exe'
        self.icon = 'dotnet.png'
        self.homepage = 'https://dot.net'

        self.direct_download_pattern = compile(
            r'https://builds\.dotnet\.microsoft\.com/dotnet/Runtime/\d+\.\d+\.\d+/dotnet-runtime-\d+\.\d+\.\d+-win-x64\.exe'
        )
        self.installer_id_pattern = compile(
            r'runtime-\d+\.\d+\.\d+-windows-x64-installer'
        )

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        try:
            error = reply.error()
            if error != QNetworkReply.NetworkError.NoError:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
                return

            html = reply.readAll().data().decode()

            if 'thank-you' in reply.url().path():
                self._handle_thank_you_page(html)
            else:
                self._handle_download_page(html)
        finally:
            reply.deleteLater()

    def _handle_thank_you_page(self, html: str):
        match = self.direct_download_pattern.search(html)
        if match:
            self.url_resolved.emit(match.group(0))
        else:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)

    def _handle_download_page(self, html: str):
        match = self.installer_id_pattern.search(html)
        if match:
            thank_you_url = f'https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/{match.group(0)}'
            self.manager.get(QNetworkRequest(thank_you_url))
        else:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://dotnet.microsoft.com/en-us/download/dotnet/9.0'))
