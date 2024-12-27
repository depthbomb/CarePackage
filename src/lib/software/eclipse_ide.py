from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class EclipseIDE(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'eclipse-ide'
        self.name = 'Eclipse IDE'
        self.category = SoftwareCategory.Development
        self.download_name = 'eclipse-inst-jre-win64.exe'
        self.is_archive = False
        self.should_cache_url = True
        self.requires_admin = False
        self.icon = 'eclipse-ide.png'
        self.homepage = 'https://eclipseide.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        version_pattern = compile(r'https://www\.eclipse.org/downloads/download\.php\?file=/oomph/epp/(\d{4}-\d+)/R/eclipse-inst-jre-win64.exe')
        html = reply.readAll().data().decode()
        match = version_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(f'https://www.eclipse.org/downloads/download.php?file=/oomph/epp/{match.group(1)}/R/eclipse-inst-jre-win64.exe&r=1')

    def resolve_download_url(self):
        self.manager.get(QNetworkRequest('https://www.eclipse.org/downloads/packages/'))
