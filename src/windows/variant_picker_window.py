from src.lib import win32
from typing import cast, Optional
from PySide6.QtGui import QIcon, QPixmap
from src.lib.software import BaseSoftware
from PySide6.QtCore import Qt, Slot, QObject
from PySide6.QtWidgets import QLabel, QDialog, QWidget, QCheckBox, QGroupBox, QPushButton, QVBoxLayout, QHBoxLayout, QScrollArea

class VariantPickerWindow(QDialog):
    def __init__(self, parent_software: BaseSoftware, variants: list[BaseSoftware], current_selection: list[BaseSoftware], parent: Optional[QObject] = None):
        super().__init__(parent)

        self.parent_software = parent_software
        self.variants = variants
        self.current_selection = current_selection
        self.selected_variants = cast(list[BaseSoftware], [])

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setSpacing(12)
        self.main_layout.setContentsMargins(11, 11, 11, 11)

        self.variants_group = QGroupBox('Available Variants')
        self.variants_layout = QVBoxLayout(self.variants_group)
        self.variants_layout.setSpacing(6)

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
            checkbox_layout.addWidget(checkbox, 1)

            self.variants_layout.addLayout(checkbox_layout)

        if len(self.variants) > 8:
            self.scroll_area = QScrollArea()
            self.scroll_widget = QWidget()
            self.scroll_widget.setLayout(self.variants_layout)
            self.scroll_area.setWidget(self.scroll_widget)
            self.scroll_area.setWidgetResizable(True)
            self.scroll_area.setMaximumHeight(200)
            self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

            self.group_scroll_layout = QVBoxLayout(self.variants_group)
            self.group_scroll_layout.addWidget(self.scroll_area)

        self.main_layout.addWidget(self.variants_group)

        self.button_layout = QHBoxLayout()
        self.button_layout.setSpacing(6)
        self.button_layout.addStretch()

        self.continue_button = QPushButton('&Continue')
        self.continue_button.setDefault(True)
        self.continue_button.setMinimumWidth(75)
        self.continue_button.clicked.connect(self._on_continue_button_clicked)

        self.cancel_button = QPushButton('Cancel')
        self.cancel_button.setMinimumWidth(75)
        self.cancel_button.clicked.connect(self._on_cancel_button_clicked)

        self.button_layout.addWidget(self.continue_button)
        self.button_layout.addWidget(self.cancel_button)

        self.main_layout.addLayout(self.button_layout)

        base_height = 100
        content_height = len(self.variants) * 25
        if len(self.variants) > 8:
            content_height = 200

        self.setMinimumWidth(350)
        self.setMaximumWidth(500)
        self.resize(400, base_height + content_height)
        self.adjustSize()
        self.setFixedSize(self.size())
        self.setWindowTitle(f'Select Variants - {self.parent_software.name}')
        self.setWindowIcon(QIcon(QPixmap(f':images/software/{self.parent_software.icon}')))

    #region Overrides
    def showEvent(self, event):
        win32.use_immersive_dark_mode(self)
        super().showEvent(event)

    def closeEvent(self, event):
        self.reject()
        event.accept()

    def reject(self):
        self.selected_variants = []
        super().reject()
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

    @Slot()
    def _on_continue_button_clicked(self):
        self.accept()

    @Slot()
    def _on_cancel_button_clicked(self):
        self.reject()
    #endregion
