from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class SublimeText(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'sublime-text'
        self.name = 'Sublime Text'
        self.category = SoftwareCategory.Development
        self.download_name = 'sublime_text_build_x64_setup.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = True
        self.icon = 'sublime-text.png'
        self.homepage = 'https://sublimetext.com'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://download\.sublimetext\.com/sublime_text_build_\d+_x64_setup.exe')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.sublimetext.com/download_thanks?target=win-x64'))
