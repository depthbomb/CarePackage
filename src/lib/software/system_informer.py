from re import compile
from PySide6.QtCore import Slot, QUrl
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class SystemInformer(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'system-informer'
        self.name = 'System Informer'
        self.category = SoftwareCategory.Utility
        self.download_name = 'systeminformer-setup.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'system-informer.png'
        self.homepage = 'https://systeminformer.sourceforge.io'

        self._initial_url = QUrl('https://systeminformer.sourceforge.io/downloads')

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        html = reply.readAll().data().decode()

        if reply.url() == self._initial_url:
            download_file_name_pattern = compile(r'https://sourceforge\.net/projects/systeminformer/files/(systeminformer-\d+\.\d+\.\d+-release-setup\.exe)/download')
            match = download_file_name_pattern.search(html)
            if not match:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            else:
                req = QNetworkRequest(f'https://sourceforge.net/settings/mirror_choices?projectname=systeminformer&filename={match.group(1)}&selected=auto&dialog=true')
                self.manager.get(req)
        else:
            download_url_pattern = compile(r'<a href="(.*)" rel="nofollow">')
            match = download_url_pattern.search(html)
            if not match:
                self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            else:
                self.url_resolved.emit(match.group(1))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://systeminformer.sourceforge.io/downloads'))
