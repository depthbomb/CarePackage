from typing import Optional
from PySide6.QtCore import Qt, QObject
from PySide6.QtGui import QFont, QPixmap
from src.widgets.simple_link_label import SimpleLinkLabel
from PySide6.QtWidgets import QLabel, QDialog, QVBoxLayout
from src import APP_REPO_URL, APP_DISPLAY_NAME, APP_VERSION_STRING

class AboutWindow(QDialog):
    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)

        self.layout = QVBoxLayout(self)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.logo = QLabel(self)
        self.logo.setFixedSize(64, 64)
        self.logo.setScaledContents(True)
        self.logo.setPixmap(QPixmap(':images/icon.png'))

        self.title_label = QLabel(APP_DISPLAY_NAME, self)
        self.title_label.setFont(QFont(self.title_label.font().family(), 16, QFont.Weight.DemiBold))

        self.version_label = QLabel(APP_VERSION_STRING, self)

        self.repo_link = SimpleLinkLabel('GitHub', APP_REPO_URL)

        self.layout.addWidget(self.logo, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(self.version_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(self.repo_link, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(self.layout)
        self.setWindowTitle('About')
        self.setFixedSize(200, 200)
