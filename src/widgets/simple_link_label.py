from typing import Optional
from PySide6.QtCore import Slot, QObject
from PySide6.QtGui import QDesktopServices
from src.widgets.link_label import LinkLabel

class SimpleLinkLabel(LinkLabel):
    def __init__(self, text: str, url: str, parent: Optional[QObject] = None):
        super().__init__(text, parent)

        self.url = url
        self.clicked.connect(self._on_clicked)

    @Slot()
    def _on_clicked(self):
        QDesktopServices.openUrl(self.url)

    def set_url(self, url: str):
        self.url = url
