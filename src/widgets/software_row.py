from functools import cache
from typing import cast, Optional
from src.enums import SettingsKeys
from src.lib.theme import ThemeUtil
from src.widgets.badge import Badge
from src.lib.settings import Settings
from src.lib.software import BaseSoftware
from PySide6.QtCore import Qt, Slot, Signal, QObject
from src.windows.variant_wizard import VariantWizard
from PySide6.QtGui import QFont, QIcon, QPixmap, QDesktopServices
from PySide6.QtWidgets import (
    QMenu,
    QLabel,
    QWidget,
    QHBoxLayout,
    QSizePolicy,
    QMessageBox,
    QApplication,
    QGraphicsDropShadowEffect
)

class SoftwareRow(QWidget):
    selection_changed = Signal(BaseSoftware, bool)
    variant_selection_changed = Signal(BaseSoftware, bool)

    def __init__(self, software: BaseSoftware, parent: Optional[QObject] = None):
        super().__init__(parent)

        self._generate_stylesheets()

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

        Settings().saved.connect(self._on_settings_saved)

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

    @Slot()
    def _on_settings_saved(self):
        self.badge_widget.setVisible(Settings().get(SettingsKeys.ShowCategoryBadges, True, bool))
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

    def _update_selection_style(self):
        badge_visible = Settings().get(SettingsKeys.ShowCategoryBadges, True, bool)
        if self.selected:
            self.setStyleSheet(self._selected_stylesheet)

            if badge_visible:
                self.badge_widget.setVisible(False)
        else:
            if self.hovered:
                self.setStyleSheet(self._hovered_stylesheet)
            else:
                self.setStyleSheet('')

            if badge_visible:
                self.badge_widget.setVisible(True)

    @cache
    def _generate_stylesheets(self):
        style_name = QApplication.style().name()
        is_fusion_or_windows = style_name in ('fusion', 'windows')
        is_dark = ThemeUtil.is_dark_palette()

        selected_bg_shade = 150 if is_fusion_or_windows else 175
        self._selected_stylesheet = f'''
            #SoftwareRow {{
                background: {ThemeUtil.get_accent_color_shade(ThemeUtil.Mode.Lighter, selected_bg_shade).name()};
            }}
            
            #SoftwareName {{
                color: {ThemeUtil.get_accent_color_shade(ThemeUtil.Mode.Darker, 500).name()};
                font-weight: bold;
            }}
        '''

        if is_fusion_or_windows:
            if is_dark:
                hovered_bg = ThemeUtil.get_accent_color_shade(ThemeUtil.Mode.Darker, 250).name()
                text_color = '#fff'
            else:
                hovered_bg = ThemeUtil.get_accent_color_shade(ThemeUtil.Mode.Lighter, 150).name()
                text_color = '#000'
        else:
            hovered_bg = self.palette().color(self.backgroundRole()).name()
            text_color = '#000'

        self._hovered_stylesheet = f'''
            #SoftwareRow {{
                background-color: {hovered_bg};
            }}
            
            #SoftwareName {{
                color: {text_color};
            }}
        '''
