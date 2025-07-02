from src.lib import win32
from typing import Optional
from src import APP_REPO_URL
from PySide6.QtCore import Slot, QObject
from PySide6.QtGui import QDesktopServices
from src.lib.software import SoftwareCategory
from PySide6.QtWidgets import QDialog, QComboBox, QVBoxLayout

class SuggestionWindow(QDialog):
    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)

        self.suggestion_link_template = f'{APP_REPO_URL}/issues/new?title=[%s] PROGRAM NAME'

        self.layout = QVBoxLayout(self)

        self.category_combobox = QComboBox(self)
        self.category_combobox.addItem('None', None)
        for cat in SoftwareCategory:
            self.category_combobox.addItem(cat, self.suggestion_link_template % cat)
        self.category_combobox.currentIndexChanged.connect(self._on_category_combobox_current_index_changed)

        self.layout.addWidget(self.category_combobox)

        self.setLayout(self.layout)
        self.setMinimumWidth(256)
        self.adjustSize()
        self.setFixedSize(self.size())
        self.setWindowTitle('Suggest software')

    def showEvent(self, event):
        win32.use_immersive_dark_mode(self)
        super().showEvent(event)

    @Slot(int)
    def _on_category_combobox_current_index_changed(self, index: int):
        current_data = self.category_combobox.currentData()
        if current_data is None:
            return

        QDesktopServices.openUrl(current_data)
        self.accept()
