from re import compile
from PySide6.QtCore import Slot
from src import BROWSER_USER_AGENT
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class FileZilla(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'filezilla'
        self.name = 'FileZilla'
        self.category = [SoftwareCategory.Development, SoftwareCategory.FileManagement, SoftwareCategory.Network]
        self.download_name = 'FileZilla_win64-setup.exe'
        self.icon = 'filezilla.png'
        self.homepage = 'https://filezilla-project.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://dl\d+\.cdn\.filezilla-project\.org/client/FileZilla_\d+\.\d+\.\d+_win64-setup\.exe\?h=[a-zA-Z0-9-_]{22,}&x=\d{10,}')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        req = QNetworkRequest('https://filezilla-project.org/download.php?show_all=1')
        req.setHeader(QNetworkRequest.KnownHeaders.UserAgentHeader, BROWSER_USER_AGENT)
        req.setRawHeader(b'Accept', b'*/*')

        self.manager.get(req)
