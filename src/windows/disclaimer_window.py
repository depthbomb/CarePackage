from src.lib import win32
from typing import Optional
from PySide6.QtGui import QIcon
from PySide6.QtCore import Slot, QTimer, QObject
from PySide6.QtWidgets import QMessageBox, QPushButton

class DisclaimerWindow(QMessageBox):
    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)

        self.choice_timer = QTimer(self)
        self.choice_timer.setInterval(5_000)
        self.choice_timer.setSingleShot(True)
        self.choice_timer.timeout.connect(self._on_choice_timer_timeout)
        self.choice_timer.start()

        self.setWindowTitle('Disclaimer')
        self.setWindowIcon(QIcon(':icons/icon.ico'))
        self.setIcon(QMessageBox.Icon.Information)
        self.setText('This application is an independent, open-source project and is not affiliated with, endorsed by, '
                     'or associated with the software it manages. All trademarks and software names are the property of'
                     ' their respective owners.')

        self.accept_button = QPushButton('&Accept', self)
        self.accept_button.setEnabled(False)
        self.accept_button.clicked.connect(self.accept)

        self.decline_button = QPushButton('&Decline', self)
        self.decline_button.setEnabled(False)
        self.decline_button.clicked.connect(self.reject)

        self.addButton(self.accept_button, QMessageBox.ButtonRole.AcceptRole)
        self.addButton(self.decline_button, QMessageBox.ButtonRole.RejectRole)

    #region Overrides
    def showEvent(self, event):
        win32.use_immersive_dark_mode(self)
        super().showEvent(event)

    def closeEvent(self, event):
        self.reject()
        event.accept()
    #endregion

    #region Slots
    @Slot()
    def _on_choice_timer_timeout(self):
        self.choice_timer.deleteLater()
        self.accept_button.setEnabled(True)
        self.decline_button.setEnabled(True)
    #endregion
