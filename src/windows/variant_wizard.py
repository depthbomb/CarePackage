from typing import cast, Optional
from src.lib.theme import ThemeUtil
from PySide6.QtGui import QIcon, QPixmap
from src.lib.software import BaseSoftware
from PySide6.QtCore import QObject, Qt, Slot
from src.widgets.simple_link_label import SimpleLinkLabel
from PySide6.QtWidgets import QLabel, QWizard, QCheckBox, QWizardPage, QVBoxLayout, QHBoxLayout

class VariantWizard(QWizard):
    def __init__(self, parent_software: BaseSoftware, variants: list[BaseSoftware], current_selection: list[BaseSoftware], parent: Optional[QObject] = None):
        super().__init__(parent)

        self.parent_software = parent_software
        self.variants = variants
        self.current_selection = current_selection
        self.selected_variants = cast(list[BaseSoftware], [])

        self.setWindowIcon(QIcon(':icons/icon.ico'))
        self.setWindowTitle(f'Select one or more variants/versions for {self.parent_software.name}')
        self.setWizardStyle(QWizard.WizardStyle.ModernStyle)
        self.setButtonLayout([QWizard.WizardButton.Stretch, QWizard.WizardButton.FinishButton])
        self.addPage(self._create_page())

    #region Overrides
    def showEvent(self, event):
        ThemeUtil.use_immersive_dark_mode(self)
        super().showEvent(event)
    #endregion

    #region Slots
    @Slot(bool)
    def _on_checkbox_state_changed(self, state: Qt.CheckState):
        cb = cast(QCheckBox, self.sender())
        variant = cast(BaseSoftware, cb.property('software'))
        if state == Qt.CheckState.Checked and variant not in self.selected_variants:
            self.selected_variants.append(variant)
        elif state == Qt.CheckState.Unchecked and variant in self.selected_variants:
            self.selected_variants.remove(variant)
    #endregion

    #region UI Setup
    def _create_page(self):
        self.page = QWizardPage()
        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel(
                f'<i>{self.parent_software.name}</i> has multiple variants or versions available.<br>Please select the '
                f'ones you would like to download.'
        ))
        self.layout.addSpacing(11)

        for variant in self.variants:
            checkbox_layout = QHBoxLayout()
            checkbox_layout.setSpacing(6)

            variant_icon = QLabel()
            variant_pixmap = QPixmap(f':images/software/{variant.icon}')
            if not variant_pixmap.isNull():
                small_pixmap = variant_pixmap.scaled(16, 16, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                variant_icon.setPixmap(small_pixmap)
            variant_icon.setFixedSize(16, 16)

            checkbox = QCheckBox(variant.name)
            checkbox.setProperty('software', variant)
            checkbox.setChecked(variant in self.current_selection)
            checkbox.checkStateChanged.connect(self._on_checkbox_state_changed)

            if variant in self.current_selection:
                self.selected_variants.append(variant)

            checkbox_layout.addWidget(variant_icon)
            checkbox_layout.addWidget(checkbox)

            if variant.is_archive:
                archive_badge = QLabel()
                archive_badge.setFixedSize(16, 16)
                archive_badge.setScaledContents(True)
                archive_badge.setPixmap(QPixmap(':icons/zip.ico'))
                archive_badge.setToolTip('This software is contained within a compressed archive.')
                archive_badge.setCursor(Qt.CursorShape.WhatsThisCursor)
                checkbox_layout.addWidget(archive_badge)

            homepage_link = SimpleLinkLabel('Homepage', variant.homepage)

            checkbox_layout.addStretch()
            checkbox_layout.addWidget(homepage_link)

            self.layout.addLayout(checkbox_layout)

        self.page.setLayout(self.layout)

        return self.page
    #endregion
