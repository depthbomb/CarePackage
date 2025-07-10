from typing import cast, Optional
from src import SOFTWARE_CATALOGUE
from src.lib.theme import ThemeUtil
from PySide6.QtCore import Qt, Slot, Signal
from src.lib.update_checker import UpdateChecker
from src.widgets.software_row import SoftwareRow
from PySide6.QtGui import QShortcut, QKeySequence
from src.lib.software import BaseSoftware, SoftwareCategory
from PySide6.QtWidgets import (
    QLabel,
    QWidget,
    QComboBox,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QVBoxLayout,
    QHBoxLayout,
)

class MainScreen(QWidget):
    software_selected = Signal(list)

    def __init__(self):
        super().__init__()

        self.has_selection = False

        self.update_checker = cast(Optional[UpdateChecker], None)
        self.selected_software = cast(list[BaseSoftware], [])
        self.software_widgets = cast(list[SoftwareRow], [])

        self.main_layout = QVBoxLayout()
        self.main_layout.setSpacing(8)
        self.main_layout.addWidget(self._create_header_controls())
        self.main_layout.addWidget(self._create_software_catalogue())
        self.main_layout.addWidget(self._create_footer())

        #region Shortcuts
        self.select_all_shortcut = QShortcut(QKeySequence('Ctrl+A'), self)
        self.deselect_shortcut = QShortcut(QKeySequence('Ctrl+D'), self)

        self.select_all_shortcut.activated.connect(self._on_select_all_shortcut_activated)
        self.deselect_shortcut.activated.connect(self._on_deselect_shortcut_activated)
        #endregion

        self.setLayout(self.main_layout)

    #region Overrides
    def mousePressEvent(self, event):
        focused_widget = self.focusWidget()
        if isinstance(focused_widget, QLineEdit):
            focused_widget.clearFocus()
        super().mousePressEvent(event)
    #endregion

    #region Slots
    @Slot(BaseSoftware, bool)
    def _on_software_row_selection_changed(self, software: BaseSoftware, selected: bool):
        if selected:
            if software not in self.selected_software:
                self.selected_software.append(software)
        else:
            if software in self.selected_software:
                self.selected_software.remove(software)

        self.has_selection = len(self.selected_software) > 0
        self.start_button.setEnabled(self.has_selection)
        self.reset_button.setEnabled(self.has_selection)
        self.selected_software_count.setVisible(self.has_selection)
        self.selected_software_count.setText(f'{len(self.selected_software)} software selected')

    @Slot()
    def _on_start_button_clicked(self):
        if len(self.selected_software) == 0:
            return

        self.software_selected.emit(
                [sw for sw in self.selected_software if not sw.has_variants]
        )

    @Slot()
    def _on_reset_button_clicked(self):
        self.clear_selection()

    @Slot()
    def _on_select_all_shortcut_activated(self):
        self._select_all()

    @Slot()
    def _on_deselect_shortcut_activated(self):
        self.clear_selection()

    @Slot()
    def _on_filters_changed(self):
        selected_category = self.category_picker.currentData()
        search_text = self.search_input.text().strip().lower()

        for row in self.software_widgets:
            software = row.software
            matches_category = (
                not selected_category or
                selected_category in [c.name for c in software.category]
            )
            matches_search = search_text in software.name.lower()

            if matches_category and matches_search:
                row.show()
            else:
                row.hide()
    #endregion

    #region UI Setup
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
        if self.style().name() != 'fusion':
            self.search_input.setStyleSheet(f'''
                QLineEdit:focus {{
                    border: 1px solid {ThemeUtil.get_accent_color_name()};
                }}
            ''')
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
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        if self.style().name() == 'fusion' or self.style().name() == 'windows':
            scroll_area.setStyleSheet(f'''
                QScrollArea {{ background: {self.palette().color(self.backgroundRole()).lighter(150).name()}; border: 1px solid {ThemeUtil.get_accent_color_name()}; }}
                QScrollArea > QWidget > QWidget {{ background: transparent; }}
                QScrollArea > QWidget > QScrollBar {{ background: 1; }}
            ''')
        else:
            scroll_area.setStyleSheet(f'''
                QScrollArea {{ background: #fff; border: 1px solid {ThemeUtil.get_accent_color_name()}; }}
                QScrollArea > QWidget > QWidget {{ background: transparent; }}
                QScrollArea > QWidget > QScrollBar {{ background: 1; }}
            ''')

        catalogue_widget = QWidget(self)
        catalogue_layout = QVBoxLayout(catalogue_widget)
        catalogue_layout.setSpacing(0)
        catalogue_layout.setContentsMargins(0, 0, 0, 0)
        catalogue_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        catalogue_widget.setLayout(catalogue_layout)

        for software in SOFTWARE_CATALOGUE:
            row = SoftwareRow(software, scroll_area)
            row.selection_changed.connect(self._on_software_row_selection_changed)
            row.variant_selection_changed.connect(self._on_software_row_selection_changed)

            catalogue_layout.addWidget(row)

            self.software_widgets.append(row)

        scroll_area.setWidget(catalogue_widget)

        return scroll_area

    def _create_footer(self):
        widget = QWidget(self)
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.start_button = QPushButton('&Continue')
        self.start_button.setFixedHeight(32)
        self.start_button.setEnabled(False)
        self.start_button.clicked.connect(self._on_start_button_clicked)

        self.reset_button = QPushButton('&Reset')
        self.reset_button.setFixedHeight(32)
        self.reset_button.setEnabled(False)
        self.reset_button.clicked.connect(self._on_reset_button_clicked)

        layout.addWidget(self.start_button)
        layout.addWidget(self.reset_button)

        layout.addStretch()

        widget.setLayout(layout)

        return widget
    #endregion

    def clear_selection(self):
        for widget in [w for w in self.software_widgets if w.selected is True]:
            widget.set_selection(False)

    def _select_all(self):
        for widget in [w for w in self.software_widgets if not w.has_variants]:
            if not widget.selected and widget.isVisible():
                widget.set_selection(True)

    def update_badge_visibility(self):
        for widget in self.software_widgets:
            widget.update_badge_visibility()
