from typing import cast, Optional
from PySide6.QtGui import QFont, QIcon
from src.lib.software import BaseSoftware
from src.lib.colors import get_accent_color
from src.widgets.link_label import LinkLabel
from PySide6.QtCore import Qt, Slot, QProcess
from src.lib.update_checker import UpdateChecker
from src.lib.settings import PostOperationAction
from src.widgets.software_row import SoftwareRow
from src.windows.about_window import AboutWindow
from src.windows.settings_window import SettingsWindow
from winrt.windows.ui.viewmanagement import UIColorType
from src.windows.operation_window import OperationWindow
from src.widgets.simple_link_label import SimpleLinkLabel
from src.windows.suggestion_window import SuggestionWindow
from src.lib.settings import user_settings, UserSettingsKeys
from src import IS_ADMIN, IS_ONEFILE, IS_COMPILED, SOFTWARE_CATALOGUE
from PySide6.QtWidgets import (
    QLabel,
    QStyle,
    QDialog,
    QWidget,
    QTabWidget,
    QPushButton,
    QScrollArea,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.update_checker = cast(Optional[UpdateChecker], None)
        self.selected_software = cast(list[BaseSoftware], [])
        self.software_widgets = cast(list[SoftwareRow], [])

        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self._create_header())
        self.main_layout.addWidget(self._create_software_tabs())
        self.main_layout.addWidget(self._create_footer())
        self.main_widget.setLayout(self.main_layout)

        self.setCentralWidget(self.main_widget)
        self._populate_software_rows()
        self.setWindowIcon(QIcon(':icons/icon.ico'))
        self.setMinimumSize(1100, 600)

        self._update_tab_names()

    #region Slots
    @Slot(str)
    def _on_update_available(self, url: str):
        self.update_link.set_url(url)
        self.update_link.setVisible(True)

    @Slot(BaseSoftware, bool)
    def _on_software_row_selection_changed(self, software: BaseSoftware, selected: bool):
        if selected:
            if software not in self.selected_software:
                self.selected_software.append(software)
        else:
            if software in self.selected_software:
                self.selected_software.remove(software)

        has_selection = len(self.selected_software) > 0
        self.start_button.setEnabled(has_selection)
        self.reset_button.setEnabled(has_selection)

    @Slot()
    def _on_start_button_clicked(self):
        if len(self.selected_software) == 0:
            return

        operation_dialog = OperationWindow(self.selected_software, self)
        operation_dialog.quit_requested.connect(self._on_operation_window_quit_requested)
        operation_dialog.post_op_action_requested.connect(self._on_operation_window_post_op_action_requested)
        if operation_dialog.exec() == QDialog.DialogCode.Accepted:
            self._clear_selection()

        self.raise_()
        self.setFocus()

    @Slot()
    def _on_reset_button_clicked(self):
        self._clear_selection()

    @Slot()
    def _on_select_all_button_clicked(self):
        self._select_all()

    @Slot()
    def _on_settings_link_clicked(self):
        settings_window = SettingsWindow(self)
        settings_window.exec()
        self._update_tab_names()

    @Slot()
    def _on_suggest_software_link_clicked(self):
        suggestion_window = SuggestionWindow(self)
        suggestion_window.exec()

    @Slot()
    def _on_about_link_clicked(self):
        about_window = AboutWindow(self)
        about_window.exec()

    @Slot()
    def _on_operation_window_quit_requested(self):
        self.close()

    @Slot(PostOperationAction)
    def _on_operation_window_post_op_action_requested(self, action: PostOperationAction):
        import src.lib.win32 as win32
        match action:
            case PostOperationAction.DoNothing:
                return
            case PostOperationAction.CloseApp:
                self.close()
            case PostOperationAction.LogOut:
                win32.log_out()
            case PostOperationAction.Lock:
                win32.lock()
            case PostOperationAction.Restart:
                QProcess.startDetached('shutdown', ['/r', '/t', '60'])
            case PostOperationAction.ShutDown:
                QProcess.startDetached('shutdown', ['/s', '/t', '60'])
    #endregion

    #region UI Setup
    def _create_header(self):
        widget = QWidget()
        layout = QHBoxLayout()

        color = get_accent_color(UIColorType.ACCENT_DARK1)
        label = QLabel('Select software to download')
        label.setFont(QFont(label.font().family(), 16))
        label.setObjectName('HeaderLabel')
        label.setStyleSheet(f'''
            #HeaderLabel {{
                color: {color};
                font-size: 20px;
            }}
        ''')

        if IS_ADMIN:
            admin_badge = QLabel()
            admin_badge.setScaledContents(True)
            admin_badge.setPixmap(self.style().standardPixmap(QStyle.StandardPixmap.SP_VistaShield))
            admin_badge.setToolTip('Running as administrator')
            admin_badge.setFixedSize(18, 18)
            layout.addWidget(admin_badge)

        layout.addWidget(label)

        widget.setLayout(layout)

        return widget

    def _create_software_tabs(self):
        self.software_tabs = QTabWidget(self)

        return self.software_tabs

    def _create_footer_links(self):
        footer_links_widget = QWidget(self)
        footer_links_layout = QHBoxLayout()
        footer_links_layout.setSpacing(12)
        footer_links_layout.setContentsMargins(0, 0, 0, 0)

        footer_links_widget.setLayout(footer_links_layout)

        #region Update checking
        self.update_link = SimpleLinkLabel('Update available', '', self)
        self.update_link.setVisible(False)

        footer_links_layout.addWidget(self.update_link)

        self.update_checker = UpdateChecker(self)
        self.update_checker.update_available.connect(self._on_update_available)
        self.update_checker.start_checking()
        #endregion

        self.suggestion_link = LinkLabel('Suggest software', self)
        self.suggestion_link.clicked.connect(self._on_suggest_software_link_clicked)

        self.about_link = LinkLabel('About', self)
        self.about_link.clicked.connect(self._on_about_link_clicked)

        footer_links_layout.addWidget(self.suggestion_link)
        footer_links_layout.addWidget(self.about_link)

        return footer_links_widget

    def _create_footer(self):
        widget = QWidget(self)
        layout = QHBoxLayout()

        self.start_button = QPushButton('&Continue')
        self.start_button.setEnabled(False)
        self.start_button.clicked.connect(self._on_start_button_clicked)

        self.reset_button = QPushButton('&Reset')
        self.reset_button.setEnabled(False)
        self.reset_button.clicked.connect(self._on_reset_button_clicked)

        layout.addWidget(self.start_button)
        layout.addWidget(self.reset_button)

        if not IS_COMPILED:
            self.select_all_button = QPushButton('Select all (debug)')
            self.select_all_button.clicked.connect(self._on_select_all_button_clicked)
            layout.addWidget(self.select_all_button)

        if not IS_ONEFILE:
            self.settings_link = LinkLabel('Settings', self)
            self.settings_link.clicked.connect(self._on_settings_link_clicked)
            layout.addWidget(self.settings_link)

        layout.addStretch()
        layout.addWidget(self._create_footer_links())

        widget.setLayout(layout)

        return widget
    #endregion

    def _populate_software_rows(self):
        # Sort the catalogue alphabetically but keep the .NET category as the last item
        for category, software in sorted(SOFTWARE_CATALOGUE.items(), key=lambda x: (x[0].startswith('.'), x[0])):
            scroll_area = QScrollArea(self.software_tabs)
            scroll_area.setProperty('tab_category', category)
            scroll_area.setProperty('tab_software', software)
            scroll_area.setWidgetResizable(True)
            scroll_area.setStyleSheet('''
                QScrollArea { background: transparent; }
                QScrollArea > QWidget > QWidget { background: transparent; }
                QScrollArea > QWidget > QScrollBar { background: 1; }
            ''')

            category_widget = QWidget(self)
            category_layout = QVBoxLayout(category_widget)
            category_layout.setSpacing(0)
            category_layout.setContentsMargins(0, 0, 0, 0)
            category_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            category_widget.setLayout(category_layout)

            scroll_area.setWidget(category_widget)

            for s in sorted(software, key=lambda sw: sw.name.lower()):
                row = SoftwareRow(s, category_widget)
                row.selection_changed.connect(self._on_software_row_selection_changed)
                category_layout.addWidget(row)
                self.software_widgets.append(row)

            self.software_tabs.addTab(scroll_area, f'{category} ({len(software)})')

    def _select_all(self):
        for widget in [w for w in self.software_widgets if w.selected is False]:
            widget.set_selection(True)

    def _clear_selection(self):
        for widget in [w for w in self.software_widgets if w.selected is True]:
            widget.set_selection(False)

    def _update_tab_names(self):
        for i in range(self.software_tabs.count()):
            tab_widget = self.software_tabs.widget(i)
            tab_category = cast(str, tab_widget.property('tab_category'))
            tab_software = cast(list[BaseSoftware], tab_widget.property('tab_software'))

            if user_settings.value(UserSettingsKeys.ShowCategorySoftwareCount, False, bool):
                self.software_tabs.setTabText(i, f'{tab_category} ({len(tab_software)})')
            else:
                self.software_tabs.setTabText(i, tab_category)
