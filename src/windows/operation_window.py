from ctypes import windll
from collections import deque
from src import IS_ADMIN, DOWNLOAD_DIR
from src.lib.software import BaseSoftware
from PySide6.QtCore import Qt, Slot, Signal
from src.lib.settings import PostOperationAction
from typing import cast, Deque, Optional, Sequence
from PySide6.QtGui import QCloseEvent, QDesktopServices
from src.widgets.software_progress_row import SoftwareProgressRow
from PySide6.QtWidgets import (
    QLabel,
    QWidget,
    QDialog,
    QCheckBox,
    QComboBox,
    QMessageBox,
    QScrollArea,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QApplication,
)

class OperationWindow(QDialog):
    quit_requested = Signal()
    post_op_action_requested = Signal(PostOperationAction)

    def __init__(self, software: Sequence[BaseSoftware], parent: Optional[QWidget] = None):
        super().__init__(parent)

        self.software_rows = cast(Deque[SoftwareProgressRow], deque([], len(software)))

        self.downloaded_software = cast(list[BaseSoftware], [])
        self.errored_software = cast(list[BaseSoftware], [])
        self.has_archives = len([sw for sw in software if sw.is_archive]) > 0
        self.has_elevated_installers = len([sw for sw in software if sw.requires_admin]) > 0

        self.setLayout(self._create_layout())

        for sw in software:
            software_row = SoftwareProgressRow(sw, self)
            software_row.file_downloading.connect(self._on_software_row_file_downloading)
            software_row.finished.connect(self._on_software_row_finished)

            self.software_rows.append(software_row)
            self.software_progress_layout.addWidget(software_row)

        self.setWindowFlag(Qt.WindowType.SubWindow, True)
        self.setMinimumWidth(630)
        self.adjustSize()
        self.setFixedSize(self.size())

    #region Overrides
    def closeEvent(self, event: QCloseEvent):
        event.ignore()
        self.reject()
    #endregion

    #region Slots
    @Slot(Qt.CheckState)
    def _on_options_check_state_changed(self):
        is_skip_checked = self.skip_installation_checkbox.isChecked()
        is_silent_checked = self.silent_install_checkbox.isChecked()

        self.silent_install_checkbox.setEnabled(not is_skip_checked)
        self.postinstall_cleanup_checkbox.setEnabled(not is_skip_checked)
        self.skip_installation_checkbox.setEnabled(not is_silent_checked)

        if is_skip_checked:
            self.silent_install_checkbox.setChecked(False)
            self.postinstall_cleanup_checkbox.setChecked(False)
        elif is_silent_checked:
            self.skip_installation_checkbox.setChecked(False)

    @Slot()
    def _on_start_button_clicked(self):
        if self.has_archives and not self.postinstall_open_dir_checkbox.isChecked():
            mb = QMessageBox(
                QMessageBox.Icon.Information,
                'Downloading archive files',
                'One or more of the selected programs will be downloaded as compressed archives. Would you like to open'
                ' the folder containing the downloaded files when everything is done downloading?',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel,
                self
            )
            res = mb.exec()
            if res == QMessageBox.StandardButton.Yes:
                self.postinstall_open_dir_checkbox.setChecked(True)
            elif res == QMessageBox.StandardButton.Cancel:
                return

        if (self.has_elevated_installers and not IS_ADMIN) and not self.skip_installation_checkbox.isChecked():
            mb = QMessageBox(
                QMessageBox.Icon.Warning,
                'Elevated permissions required',
                'One or more of the selected programs require administrator privileges to install. Would you like to '
                'restart CarePackage as administrator? If you choose not to, then the folder containing the downloaded '
                'programs will be opened after the other programs have finished installing.',
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No | QMessageBox.StandardButton.Cancel,
                self
            )
            res = mb.exec()
            if res == QMessageBox.StandardButton.Yes:
                windll.shell32.ShellExecuteW(None, 'runas', QApplication.arguments()[0], '', None, 1)
                self.quit_requested.emit()
                self.reject()
                return
            elif res == QMessageBox.StandardButton.Cancel:
                return
            else:
                self.postinstall_open_dir_checkbox.setChecked(True)

        self.skip_installation_checkbox.setEnabled(False)
        self.silent_install_checkbox.setEnabled(False)
        self.postinstall_cleanup_checkbox.setEnabled(False)
        self.postinstall_open_dir_checkbox.setEnabled(False)
        self.start_button.setEnabled(False)

        for row in self.software_rows:
            row.set_status('Pending')

        self._download_next_software()

    @Slot()
    def _on_cancel_button_clicked(self):
        if len(self.errored_software) > 0:
            self.accept()
        else:
            self.reject()

    @Slot(str)
    def _on_software_row_file_downloading(self, url: str):
        self.software_progress_container.ensureWidgetVisible(self.sender(), 0, 0)

    @Slot(SoftwareProgressRow.OperationError)
    def _on_software_row_finished(self, error: SoftwareProgressRow.OperationError):
        software_row = cast(SoftwareProgressRow, self.sender())
        if error != SoftwareProgressRow.OperationError.NoError:
            self.errored_software.append(software_row.software)
        else:
            self.downloaded_software.append(software_row.software)
            software_row.deleteLater()

        if len(self.software_rows) == 0:
            self.cancel_button.setText('&Close')

            if self.postinstall_open_dir_checkbox.isChecked() and len(self.downloaded_software) > 0:
                QDesktopServices.openUrl(DOWNLOAD_DIR.as_posix())

            if len(self.errored_software) > 0:
                mb = QMessageBox(self)
                mb.setIcon(QMessageBox.Icon.Critical)
                mb.setWindowTitle('Errors encountered during operation')
                mb.setText(
                    'One or more errors occurred while downloading or installing the selected software.\nIf the problem'
                    ' persists then please open an issue on GitHub.'
                )
                mb.setDetailedText('\n'.join([sw.name for sw in self.errored_software]))
                mb.exec()
            else:
                self.post_op_action_requested.emit(self.post_op_combobox.currentData())
                self.accept()
        else:
            self._download_next_software()
    #endregion

    #region UI Setup
    def _create_layout(self):
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self._create_controls())
        self.layout.addWidget(self._create_software_progress_display())
        self.layout.addWidget(self._create_buttons())

        return self.layout

    def _create_controls(self):
        self.controls_widget = QWidget(self)
        self.controls_layout = QFormLayout(self.controls_widget)

        self.skip_installation_checkbox = QCheckBox('Skip installation (download only)', self)
        self.skip_installation_checkbox.checkStateChanged.connect(self._on_options_check_state_changed)

        self.silent_install_checkbox = QCheckBox('Try to install silently', self)
        self.silent_install_checkbox.checkStateChanged.connect(self._on_options_check_state_changed)

        self.postinstall_cleanup_checkbox = QCheckBox('Delete executables after installation', self)
        self.postinstall_cleanup_checkbox.checkStateChanged.connect(self._on_options_check_state_changed)

        self.postinstall_open_dir_checkbox = QCheckBox('Show downloaded files when finished', self)
        self.postinstall_open_dir_checkbox.checkStateChanged.connect(self._on_options_check_state_changed)

        self.controls_layout.addWidget(self.skip_installation_checkbox)
        self.controls_layout.addWidget(self.silent_install_checkbox)
        self.controls_layout.addWidget(self.postinstall_cleanup_checkbox)
        self.controls_layout.addWidget(self.postinstall_open_dir_checkbox)

        return self.controls_widget

    def _create_software_progress_display(self):
        self.software_progress_container = QScrollArea(self)
        self.software_progress_container.setFixedHeight(200)
        self.software_progress_container.setWidgetResizable(True)
        self.software_progress_container.setStyleSheet('''
            QScrollArea { background: #fff; }
            QScrollArea > QWidget > QWidget { background: transparent; }
            QScrollArea > QWidget > QScrollBar { background: 1; }
        ''')

        self.software_progress_widget = QWidget(self)

        self.software_progress_layout = QVBoxLayout(self.software_progress_widget)
        self.software_progress_layout.setSpacing(0)
        self.software_progress_layout.setContentsMargins(0, 0, 0, 0)
        self.software_progress_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.software_progress_widget.setLayout(self.software_progress_layout)
        self.software_progress_container.setWidget(self.software_progress_widget)

        return self.software_progress_container

    def _create_buttons(self):
        self.buttons_widget = QWidget(self)
        self.buttons_layout = QHBoxLayout(self.buttons_widget)
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)

        self.post_op_label = QLabel('When Done:', self)
        self.post_op_combobox = QComboBox(self)
        self.post_op_combobox.addItem('Do nothing', PostOperationAction.DoNothing)
        self.post_op_combobox.addItem('Quit', PostOperationAction.CloseApp)
        self.post_op_combobox.addItem('Log Out', PostOperationAction.LogOut)
        self.post_op_combobox.addItem('Lock system', PostOperationAction.Lock)
        self.post_op_combobox.addItem('Restart', PostOperationAction.Restart)
        self.post_op_combobox.addItem('Shut down system', PostOperationAction.ShutDown)
        self.post_op_combobox.setCurrentIndex(0)

        self.start_button = QPushButton('&Start', self)
        self.start_button.clicked.connect(self._on_start_button_clicked)

        self.cancel_button = QPushButton('&Cancel', self)
        self.cancel_button.clicked.connect(self._on_cancel_button_clicked)

        self.buttons_layout.addWidget(self.post_op_label)
        self.buttons_layout.addWidget(self.post_op_combobox)

        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.start_button)
        self.buttons_layout.addWidget(self.cancel_button)
        self.buttons_widget.setLayout(self.buttons_layout)

        return self.buttons_widget
    #endregion

    def _download_next_software(self):
        try:
            software_row = self.software_rows.popleft()
            software_row.start_download(
                self.skip_installation_checkbox.isChecked(),
                self.silent_install_checkbox.isChecked(),
                self.postinstall_cleanup_checkbox.isChecked(),
            )
        except IndexError:
            pass
