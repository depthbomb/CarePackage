from src import SOFTWARE_CATALOGUE
from src.lib.theme import ThemeUtil
from src.lib.settings import Settings
from PySide6.QtCore import Qt, Slot, Signal
from src.lib.software import SoftwareCategory
from src.lib.software_spec import SoftwareSpec
from PySide6.QtGui import QKeySequence, QShortcut
from src.windows.variant_wizard import VariantWizard
from src.widgets.software_catalogue_view import SoftwareCatalogueFilterModel, SoftwareCatalogueModel, SoftwareCatalogueView
from PySide6.QtWidgets import (
    QLabel,
    QWidget,
    QComboBox,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QHBoxLayout,
    QVBoxLayout,
)

class MainScreen(QWidget):
    software_selected = Signal(list)

    def __init__(self):
        super().__init__()

        self.has_selection = False
        self.selected_software: list[SoftwareSpec] = []

        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(8)
        self.main_layout.addWidget(self._create_header_controls())
        self.main_layout.addWidget(self._create_software_catalogue())
        self.main_layout.addWidget(self._create_footer())

        self.select_all_shortcut = QShortcut(QKeySequence('Ctrl+A'), self)
        self.deselect_shortcut = QShortcut(QKeySequence('Ctrl+D'), self)
        self.select_all_shortcut.activated.connect(self._select_all)
        self.deselect_shortcut.activated.connect(self.clear_selection)

        self.setLayout(self.main_layout)

    def mousePressEvent(self, event):
        focused_widget = self.focusWidget()
        if isinstance(focused_widget, QLineEdit):
            focused_widget.clearFocus()
        super().mousePressEvent(event)

    @Slot(object)
    def _on_software_activated(self, software: SoftwareSpec):
        selected = software in self.selected_software or any(
            variant in self.selected_software for variant in software.variants
        )

        if software.is_deprecated and not selected:
            message = 'This software has been deprecated and is no longer recommended.'
            if software.alternative_name:
                message += f' It is recommended that you download {software.alternative_name} instead.'
            message += '\nWould you like to keep this software selected?'

            result = QMessageBox.question(
                self,
                'Deprecated software',
                message,
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )
            if result != QMessageBox.StandardButton.Yes:
                return

        if software.has_variants:
            current_variants = [variant for variant in software.variants if variant in self.selected_software]
            wizard = VariantWizard(software, software.variants, current_variants, self)
            wizard.exec()

            self.selected_software = [
                selected_software
                for selected_software in self.selected_software
                if selected_software not in software.variants
            ]
            self.selected_software.extend(wizard.selected_variants)
            wizard.deleteLater()
        elif selected:
            self.selected_software.remove(software)
        else:
            self.selected_software.append(software)

        self._refresh_selection()

    @Slot()
    def _on_start_button_clicked(self):
        if not self.selected_software:
            return

        self.software_selected.emit([software.get_instance() for software in self.selected_software])

    @Slot()
    def _on_filters_changed(self):
        self.catalogue_filter.set_filters(
            self.category_picker.currentData(),
            self.search_input.text(),
        )

    def _create_header_controls(self):
        header_widget = QWidget()
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 0, 0, 0)

        self.search_input = QLineEdit()
        self.search_input.setFixedSize(200, 28)
        self.search_input.setFocusPolicy(Qt.FocusPolicy.ClickFocus)
        self.search_input.setPlaceholderText('Search software')
        self.search_input.setClearButtonEnabled(True)
        self.search_input.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.search_input.textChanged.connect(self._on_filters_changed)

        self.category_picker = QComboBox()
        self.category_picker.setFixedSize(200, 28)
        self.category_picker.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        self.category_picker.addItem('All Categories', '')
        for category in SoftwareCategory:
            self.category_picker.addItem(category, category.name)
        self.category_picker.currentIndexChanged.connect(self._on_filters_changed)

        self.selected_software_count = QLabel()
        self.selected_software_count.setVisible(False)

        header_layout.addWidget(self.search_input)
        header_layout.addWidget(self.category_picker)
        header_layout.addStretch()
        header_layout.addWidget(self.selected_software_count)
        header_widget.setLayout(header_layout)
        return header_widget

    def _create_software_catalogue(self):
        self.catalogue_model = SoftwareCatalogueModel(SOFTWARE_CATALOGUE, self)
        self.catalogue_filter = SoftwareCatalogueFilterModel(self)
        self.catalogue_filter.setSourceModel(self.catalogue_model)

        self.catalogue_view = SoftwareCatalogueView()
        self.catalogue_view.setModel(self.catalogue_filter)
        self.catalogue_view.software_activated.connect(self._on_software_activated)

        background = (
            self.palette().color(self.backgroundRole()).lighter(150).name()
            if ThemeUtil.style_supports_dark_mode()
            else '#fff'
        )
        self.catalogue_view.setStyleSheet(f'''
            QListView {{
                background: {background};
                border: 1px solid {ThemeUtil.get_accent_color_name()};
                outline: 0;
            }}
            QListView > QScrollBar {{ background: 1; }}
        ''')

        Settings().saved.connect(self.catalogue_view.refresh_badges)
        return self.catalogue_view

    def _create_footer(self):
        widget = QWidget()
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.start_button = QPushButton('&Continue')
        self.start_button.setFixedHeight(32)
        self.start_button.setEnabled(False)
        self.start_button.clicked.connect(self._on_start_button_clicked)

        self.reset_button = QPushButton('&Reset')
        self.reset_button.setFixedHeight(32)
        self.reset_button.setEnabled(False)
        self.reset_button.clicked.connect(self.clear_selection)

        layout.addWidget(self.start_button)
        layout.addWidget(self.reset_button)
        layout.addStretch()
        widget.setLayout(layout)
        return widget

    def clear_selection(self):
        if not self.selected_software:
            return
        self.selected_software.clear()
        self._refresh_selection()

    def _select_all(self):
        for software in self.catalogue_filter.visible_software():
            if not software.has_variants and software not in self.selected_software:
                self.selected_software.append(software)
        self._refresh_selection()

    def _refresh_selection(self):
        selected = set(self.selected_software)
        selected_rows = {
            software
            for software in SOFTWARE_CATALOGUE
            if software in selected or any(variant in selected for variant in software.variants)
        }
        self.catalogue_model.set_selected(selected_rows)

        self.has_selection = bool(self.selected_software)
        self.start_button.setEnabled(self.has_selection)
        self.reset_button.setEnabled(self.has_selection)
        self.selected_software_count.setVisible(self.has_selection)
        self.selected_software_count.setText(f'{len(self.selected_software)} software selected')
