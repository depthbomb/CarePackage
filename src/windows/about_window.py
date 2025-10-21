from typing import Optional
from src.lib.theme import ThemeUtil
from PySide6.QtCore import Qt, QObject
from PySide6.QtGui import QFont, QPixmap
from src.widgets.simple_link_label import SimpleLinkLabel
from PySide6.QtWidgets import QLabel, QDialog, QVBoxLayout
from src import APP_REPO_URL, APP_DISPLAY_NAME, APP_NEW_ISSUE_URL, APP_VERSION_STRING

class AboutWindow(QDialog):
    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.logo = QLabel()
        self.logo.setFixedSize(72, 72)
        self.logo.setScaledContents(True)
        self.logo.setPixmap(QPixmap(':images/icon.png'))

        self.title_label = QLabel(APP_DISPLAY_NAME)
        self.title_label.setFont(QFont(self.title_label.font().family(), 16, QFont.Weight.DemiBold))

        self.version_label = QLabel(APP_VERSION_STRING)

        self.repo_link = SimpleLinkLabel('GitHub', APP_REPO_URL)
        self.new_issue_link = SimpleLinkLabel('Report an issue/suggest software', APP_NEW_ISSUE_URL)

        self.layout.addWidget(self.logo, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(self.version_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(self.repo_link, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(self.new_issue_link, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(self.layout)
        self.setWindowTitle('About')
        self.setFixedSize(256, 256)

    def showEvent(self, event):
        ThemeUtil.use_immersive_dark_mode(self)
        super().showEvent(event)
