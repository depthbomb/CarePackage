from typing import cast, Optional

from lib.theme import ThemeUtil
from src.widgets.badge import Badge
from src.lib.software import BaseSoftware
from PySide6.QtCore import Qt, Slot, Signal, QObject
from src.windows.variant_wizard import VariantWizard
from src.lib.settings import user_settings, UserSettingsKeys
from PySide6.QtGui import QFont, QIcon, QPixmap, QDesktopServices
from PySide6.QtWidgets import QMenu, QLabel, QWidget, QHBoxLayout, QSizePolicy, QMessageBox, QGraphicsDropShadowEffect

SELECTED_STYLESHEET = f'''
    #SoftwareRow {{
        background: {ThemeUtil.get_accent_color_shade(ThemeUtil.Mode.Lighter, 175).name()};
    }}
    
    #SoftwareName {{
        color: {ThemeUtil.get_accent_color_shade(ThemeUtil.Mode.Darker, 500).name()};
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
    variant_selection_changed = Signal(BaseSoftware, bool)

    def __init__(self, software: BaseSoftware, parent: Optional[QObject] = None):
        super().__init__(parent)

        self.software = software
        self.has_variants = self.software.has_variants
        self.selected_variants = cast(list[BaseSoftware], [])
        self.hovered = False
        self.selected = False

        self.menu = QMenu(self)
        self.menu.addAction(QIcon(':images/open.png'), 'Homepage', self._on_homepage_action_clicked)

        self.image_shadow = QGraphicsDropShadowEffect(self)
        self.image_shadow.setOffset(0, 0)
        self.image_shadow.setBlurRadius(6)

        self.image = QLabel(self)
        self.image.setFixedSize(32, 32)
        self.image.setPixmap(QPixmap(f':images/software/{self.software.icon}'))
        self.image.setGraphicsEffect(self.image_shadow)

        self.name = QLabel(self.software.name, self)
        self.name.setObjectName('SoftwareName')
        self.name.setFont(QFont(self.name.font().family(), 13))

        self.layout = QHBoxLayout(self)
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

        if self.software.is_archive:
            archive_badge = QLabel(self)
            archive_badge.setFixedSize(16, 16)
            archive_badge.setScaledContents(True)
            archive_badge.setPixmap(QPixmap(':icons/zip.ico'))
            archive_badge.setToolTip('This software is contained within a compressed archive.')
            archive_badge.setCursor(Qt.CursorShape.WhatsThisCursor)
            self.layout.addWidget(archive_badge, alignment=Qt.AlignmentFlag.AlignVCenter)

        self.layout.addStretch()

        self.badge_widget = QWidget(self)
        self.badge_layout = QHBoxLayout(self.badge_widget)
        self.badge_layout.setSpacing(3)
        for category in self.software.category:
            badge = Badge(category.value, parent=self.badge_widget)
            self.badge_layout.addWidget(badge)
        self.badge_widget.setLayout(self.badge_layout)

        self.layout.addWidget(self.badge_widget)

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
                    alt_sw = self.software.alternative
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
            elif self.has_variants:
                # Show a special window for selecting variants
                wizard = VariantWizard(self.software, self.software.variants, self.selected_variants, self)
                wizard.exec()

                self.selected_variants = wizard.selected_variants
                for variant in self.software.variants:
                    self.variant_selection_changed.emit(variant, variant in self.selected_variants)

                self.selected = len(self.selected_variants) > 0
                self._update_selection_style()

                wizard.deleteLater()
            else:
                self.set_selection(not self.selected)
        elif event.button() == Qt.MouseButton.RightButton:
            self.menu.exec(event.globalPos())
    #endregion

    #region Slots
    @Slot()
    def _on_homepage_action_clicked(self):
        QDesktopServices.openUrl(self.software.homepage)
    #endregion

    def set_selection(self, selected: bool):
        if self.has_variants:
            for variant in self.selected_variants:
                self.variant_selection_changed.emit(variant, selected)

            if not selected:
                self.selected_variants = []

        self.selected = selected
        self.selection_changed.emit(self.software, self.selected)
        self._update_selection_style()

    def set_badge_visibility(self, visible: bool):
        self.badge_widget.setVisible(visible)

    def update_badge_visibility(self):
        visible = user_settings.value(UserSettingsKeys.ShowCategoryBadges, True, bool)
        self.badge_widget.setVisible(visible)

    def _update_selection_style(self):
        badge_visible = user_settings.value(UserSettingsKeys.ShowCategoryBadges, True, bool)
        if self.selected:
            self.setStyleSheet(SELECTED_STYLESHEET)

            if badge_visible:
                self.badge_widget.setVisible(False)
        else:
            if self.hovered:
                self.setStyleSheet(HOVERED_STYLESHEET)
            else:
                self.setStyleSheet('')

            if badge_visible:
                self.badge_widget.setVisible(True)
