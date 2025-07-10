from src.lib import win32
from typing import cast, Optional
from PySide6.QtCore import Slot, QUrl
from src.enums import PostOperationAction
from src.lib.software import BaseSoftware
from src.screens.main_screen import MainScreen
from src.lib.update_checker import UpdateChecker
from src.windows.about_window import AboutWindow
from src.widgets.header_button import HeaderButton
from PySide6.QtGui import Qt, QIcon, QDesktopServices
from src.windows.settings_window import SettingsWindow
from src.windows.extended_window import ExtendedWindow
from src.widgets.draggable_region import DraggableWidget
from src.screens.operation_screen import OperationScreen
from PySide6.QtWidgets import QWidget, QMessageBox, QHBoxLayout, QStackedWidget

class MainWindow(ExtendedWindow):
    def __init__(self):
        super().__init__()

        self.updater = UpdateChecker(self)
        self.updater.update_available.connect(self._on_update_available)
        self.updater.start_checking()

        self.drag_region = DraggableWidget()
        self.update_button = HeaderButton('download', 'Update available!')
        self.update_button.setVisible(False)
        self.update_button.clicked.connect(self._on_update_button_clicked)
        self.about_button = HeaderButton('info', 'About')
        self.about_button.clicked.connect(self._on_about_button_clicked)
        self.settings_button = HeaderButton('settings', 'Settings')
        self.settings_button.clicked.connect(self._on_settings_button_clicked)

        self.main_screen = MainScreen()
        self.main_screen.software_selected.connect(self._on_software_selected)
        self.operation_screen = cast(Optional[OperationScreen], None)

        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.main_screen)

        self.set_extended_widget(self._create_header())
        self.setCentralWidget(self.stack)
        self.setWindowIcon(QIcon(':icons/icon.ico'))
        self.setWindowTitle('CarePackage')
        self.setMinimumSize(1000, 550)

    #region Overrides
    def nativeEvent(self, eventType, message):
        res = self.drag_region.handle_native_event(eventType, message)
        if res[0]:
            return res

        return super().nativeEvent(eventType, message)
    #endregion

    #region Slots
    @Slot()
    def _on_update_button_clicked(self):
        QDesktopServices.openUrl(QUrl(self.updater.latest_release_url))

    @Slot()
    def _on_about_button_clicked(self):
        about_window = AboutWindow(self)
        about_window.exec()

    @Slot()
    def _on_settings_button_clicked(self):
        settings_window = SettingsWindow(self)
        settings_window.exec()

    @Slot(list)
    def _on_software_selected(self, software: list[BaseSoftware]):
        if self.operation_screen is None:
            self.operation_screen = OperationScreen(software)
            self.operation_screen.started.connect(self._on_operation_started)
            self.operation_screen.post_op_action_requested.connect(self._on_operation_screen_post_op_action_requested)
            self.operation_screen.finished.connect(self._on_operation_finished)
            self.stack.addWidget(self.operation_screen)
            self.stack.setCurrentIndex(1)

    @Slot()
    def _on_operation_started(self):
        self.settings_button.setEnabled(False)

    @Slot(PostOperationAction)
    def _on_operation_screen_post_op_action_requested(self, action: PostOperationAction):
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
                win32.schedule_shutdown(60, 'CarePackage has scheduled a system restart.', True)
            case PostOperationAction.ShutDown:
                win32.schedule_shutdown(30, 'CarePackage has scheduled a system shutdown.')

    @Slot(bool)
    def _on_operation_finished(self, success: bool):
        if success:
            self.main_screen.clear_selection()

        if self.operation_screen is not None:
            self.stack.removeWidget(self.operation_screen)
            self.operation_screen.post_op_action_requested.disconnect()
            self.operation_screen.finished.disconnect()
            self.operation_screen.deleteLater()
            self.operation_screen = None

        self.stack.setCurrentIndex(0)
        self.settings_button.setEnabled(True)

    @Slot()
    def _on_update_available(self):
        if self.updater.is_first_check:
            mb = QMessageBox(
                QMessageBox.Icon.Information,
                'Update available',
                'A new version of CarePackage is available. Would you like to open the download page now?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                self
            )
            res = mb.exec()
            if res == QMessageBox.StandardButton.Yes:
                QDesktopServices.openUrl(QUrl(self.updater.latest_release_url))

        self.update_button.setVisible(True)
    #endregion

    #region UI Setup
    def _create_header(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0 ,0)
        layout.setSpacing(0)
        layout.addWidget(self.drag_region)
        layout.addWidget(self.update_button, alignment=Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(self.about_button, alignment=Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(self.settings_button, alignment=Qt.AlignmentFlag.AlignVCenter)

        widget = QWidget(self)
        widget.setFixedHeight(self.extended_height)
        widget.setLayout(layout)

        return widget
    #endregion
