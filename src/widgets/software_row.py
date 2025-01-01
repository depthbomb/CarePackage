from typing import Optional
from src.lib.software import BaseSoftware
from PySide6.QtCore import Qt, Slot, Signal
from src.lib.colors import get_accent_color
from winrt.windows.ui.viewmanagement import UIColorType
from PySide6.QtGui import QFont, QPixmap, QDesktopServices
from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QHBoxLayout, QSizePolicy, QMessageBox

SELECTED_STYLESHEET = f'''
    #SoftwareRow {{
        background-color: {get_accent_color(UIColorType.ACCENT_LIGHT3)};
    }}
    
    #SoftwareName {{
        color: {get_accent_color(UIColorType.ACCENT_DARK3)};
        font-weight: bold;
    }}
'''
HOVERED_STYLESHEET = f'''
    #SoftwareRow {{
        background-color: #f0f0f0;
    }}
    
    #SoftwareName {{
        color: #000;
    }}
'''

class SoftwareRow(QWidget):
    selection_changed = Signal(BaseSoftware, bool)

    def __init__(self, software: BaseSoftware, parent: Optional[QWidget] = None):
        super().__init__(parent)

        self.software = software
        self.hovered = False
        self.selected = False

        self.image = QLabel()
        self.image.setFixedSize(32, 32)
        self.image.setPixmap(QPixmap(f':images/software/{self.software.icon}'))

        self.name = QLabel(self.software.name)
        self.name.setObjectName('SoftwareName')
        self.name.setFont(QFont(self.name.font().family(), 13))

        self.homepage_button = QPushButton('Homepage', self)
        self.homepage_button.clicked.connect(self._on_homepage_button_clicked)

        self.layout = QHBoxLayout()
        self.layout.setSpacing(12)
        self.layout.addWidget(self.image)
        self.layout.addWidget(self.name)

        if self.software.is_deprecated:
            warning_badge = QLabel(self)
            warning_badge.setFixedSize(16, 16)
            warning_badge.setScaledContents(True)
            warning_badge.setPixmap(QPixmap(':icons/warning.ico'))
            warning_badge.setToolTip('This software is deprecated and no longer recommended.')
            warning_badge.setCursor(Qt.CursorShape.WhatsThisCursor)
            self.layout.addWidget(warning_badge, alignment=Qt.AlignmentFlag.AlignVCenter)

        if self.software.requires_admin:
            admin_badge = QLabel(self)
            admin_badge.setFixedSize(16, 16)
            admin_badge.setScaledContents(True)
            admin_badge.setPixmap(QPixmap(':icons/uac.ico'))
            admin_badge.setToolTip('This software requires administrator privileges to install.')
            admin_badge.setCursor(Qt.CursorShape.WhatsThisCursor)
            self.layout.addWidget(admin_badge, alignment=Qt.AlignmentFlag.AlignVCenter)
        elif self.software.is_archive:
            archive_badge = QLabel(self)
            archive_badge.setFixedSize(16, 16)
            archive_badge.setScaledContents(True)
            archive_badge.setPixmap(QPixmap(':icons/zip.ico'))
            archive_badge.setToolTip('This software is contained within a compressed archive.')
            archive_badge.setCursor(Qt.CursorShape.WhatsThisCursor)
            self.layout.addWidget(archive_badge, alignment=Qt.AlignmentFlag.AlignVCenter)

        self.layout.addStretch()
        self.layout.addWidget(self.homepage_button)

        self.setObjectName('SoftwareRow')
        self.setFixedHeight(64)
        self.setLayout(self.layout)
        self.setAttribute(Qt.WidgetAttribute.WA_Hover, True)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setMouseTracking(True)

    #region Overrides
    def enterEvent(self, event):
        self.hovered = True
        self._update_selection_style()

    def leaveEvent(self, event):
        self.hovered = False
        self._update_selection_style()

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.software.is_deprecated and not self.selected:
                message = 'This software has been deprecated and is no longer recommended.'
                if self.software.alternative:
                    alt_sw = self.software.alternative()
                    message += f' It is recommended that you download {alt_sw.name} instead.'
                    del alt_sw
                message += '\nWould you like to keep this software selected?'

                mb = QMessageBox(self)
                mb.setWindowTitle('Deprecated software')
                mb.setIcon(QMessageBox.Icon.Warning)
                mb.setText(message)
                mb.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if mb.exec() == QMessageBox.StandardButton.Yes:
                    self.set_selection(True)
            else:
                self.set_selection(not self.selected)
    #endregion

    #region Slots
    @Slot()
    def _on_homepage_button_clicked(self):
        QDesktopServices.openUrl(self.software.homepage)
    #endregion

    def set_selection(self, selected: bool):
        self.selected = selected
        self.selection_changed.emit(self.software, self.selected)
        self._update_selection_style()

    def _update_selection_style(self):
        if self.selected:
            self.setStyleSheet(SELECTED_STYLESHEET)
        else:
            if self.hovered:
                self.setStyleSheet(HOVERED_STYLESHEET)
            else:
                self.setStyleSheet('')
