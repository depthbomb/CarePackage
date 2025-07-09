from src.lib import win32
from typing import Optional
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Slot, QTimer, QObject

class DisclaimerWindow(QMessageBox):
    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)

        self.choice_timer = QTimer(self)
        self.choice_timer.setInterval(4_250)
        self.choice_timer.setSingleShot(True)
        self.choice_timer.timeout.connect(self._on_choice_timer_timeout)
        self.choice_timer.start()

        self.setWindowTitle('Disclaimer')
        self.setWindowIcon(QIcon(':icons/icon.ico'))
        self.setIcon(QMessageBox.Icon.Information)
        self.setText('This application is an independent, open-source project and is not affiliated with, endorsed by, '
                     'or associated with the software it manages. All trademarks and software names are the property of'
                     ' their respective owners.')

        self.setStandardButtons(self.StandardButton.Yes | self.StandardButton.No)
        self.setButtonText(self.StandardButton.Yes, '&Accept')
        self.setButtonText(self.StandardButton.No, '&Decline')

        self.button(self.StandardButton.Yes).setEnabled(False)
        self.button(self.StandardButton.No).setEnabled(False)

    #region Overrides
    def showEvent(self, event):
        win32.use_immersive_dark_mode(self)
        super().showEvent(event)
    #endregion

    #region Slots
    @Slot()
    def _on_choice_timer_timeout(self):
        self.button(self.StandardButton.Yes).setEnabled(True)
        self.button(self.StandardButton.No).setEnabled(True)
        self.choice_timer.deleteLater()
    #endregion
