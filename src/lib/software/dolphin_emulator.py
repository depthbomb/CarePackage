from re import compile
from PySide6.QtCore import Slot
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtNetwork import QNetworkReply, QNetworkRequest

class DolphinEmulator(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'dolphin-emulator'
        self.name = 'Dolphin Emulator'
        self.category = [SoftwareCategory.Emulation, SoftwareCategory.Gaming]
        self.download_name = 'DolphinEmu.7z'
        self.is_archive = True
        self.should_cache_url = True
        self.icon = 'dolphin-emu.png'
        self.homepage = 'https://dolphin-emu.org'

    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        reply.deleteLater()
        error = reply.error()
        if error != QNetworkReply.NetworkError.NoError:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
            return

        download_url_pattern = compile(r'https://dl\.dolphin-emu\.org/(?:releases/\d+|builds/[\da-f]{2}/[\da-f]{2})/dolphin-(?:\d+|master-\d+\.\d+-\d+)-x64\.7z')
        html = reply.readAll().data().decode()
        match = download_url_pattern.search(html)
        if not match:
            self.url_resolve_error.emit(self.ResolveError.URLResolveError)
        else:
            self.url_resolved.emit(match.group(0))

    def resolve_download_url(self):
        self.manager.get(
            QNetworkRequest('https://dolphin-emu.org/download/list/releases/1/')
        )
