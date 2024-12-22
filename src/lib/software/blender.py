from re import compile
from PySide6.QtCore import QUrl, Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class Blender(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'blender'
        self.name = 'Blender'
        self.category = SoftwareCategory.Creative
        self.download_name = 'blender-windows-x64.msi'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'blender.png'
        self.homepage = 'https://blender.org'

        self._download_page = QUrl('https://www.blender.org/download/')

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        if reply.url() == self._download_page:
            next_download_page_pattern = compile(r'https://www\.blender\.org/download/release/Blender\d+\.\d+/blender-\d\.\d+.\d+-windows-x64\.msi')
            html = reply.readAll().data().decode()
            match = next_download_page_pattern.search(html)
            if not match:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            else:
                self.manager.get(QNetworkRequest(QUrl(match.group(0))))
        else:
            download_url_pattern = compile(r'https://mirrors\.ocf\.berkeley\.edu/blender/release/Blender\d+\.\d+/blender-\d+\.\d+\.\d+-windows-x64\.msi')
            html = reply.readAll().data().decode()
            match = download_url_pattern.search(html)
            if not match:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            else:
                self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(
            QNetworkRequest(self._download_page)
        )
