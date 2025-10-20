from src import DOWNLOAD_DIR
from collections import deque
from src.lib.theme import ThemeUtil
from src.enums import PostOperationAction
from src.lib.software import BaseSoftware
from PySide6.QtGui import QDesktopServices
from PySide6.QtCore import Qt, Slot, Signal
from typing import cast, Deque, Optional, Sequence
from src.widgets.software_progress_row import SoftwareProgressRow
from PySide6.QtWidgets import (
    QLabel,
    QWidget,
    QCheckBox,
    QComboBox,
    QSizePolicy,
    QMessageBox,
    QScrollArea,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
)

class OperationScreen(QWidget):
    restart_requested = Signal(list)
    started = Signal()
    finished = Signal(bool)
    post_op_action_requested = Signal(PostOperationAction)

    def __init__(self, software: Sequence[BaseSoftware], parent: Optional[QWidget] = None):
        super().__init__(parent)

        self.canceled = False
        self.software = software
        self.software_rows = cast(Deque[SoftwareProgressRow], deque([], len(software)))
        self.pending_software = cast(Deque[SoftwareProgressRow], deque())
        self.active_downloads = cast(list[SoftwareProgressRow], [])

        self.pending_installations = cast(Deque[SoftwareProgressRow], deque())
        self.active_installation = cast(Optional[SoftwareProgressRow], None)

        self.downloaded_software = cast(list[BaseSoftware], [])
        self.errored_software = cast(list[BaseSoftware], [])
        self.has_archives = len([sw for sw in software if sw.is_archive]) > 0

        self.setLayout(self._create_layout())

        for sw in software:
            software_row = SoftwareProgressRow(sw)
            software_row.finished.connect(self._on_software_row_finished)
            software_row.installation_requested.connect(self._on_installation_requested)

            self.software_rows.append(software_row)
            self.software_progress_layout.addWidget(software_row)

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
        DOWNLOAD_DIR.mkdir(exist_ok=True)

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

        self.skip_installation_checkbox.setEnabled(False)
        self.silent_install_checkbox.setEnabled(False)
        self.postinstall_cleanup_checkbox.setEnabled(False)
        self.postinstall_open_dir_checkbox.setEnabled(False)
        self.start_button.setEnabled(False)

        self.pending_software = self.software_rows.copy()
        for row in self.pending_software:
            row.set_status('Pending', True)

        self.started.emit()

        self._start_next_downloads()

    @Slot()
    def _on_cancel_button_clicked(self):
        self.canceled = True

        for software in self.active_downloads:
            software.cancel()

        if len(self.errored_software) > 0:
            self.finished.emit(True)
        else:
            self.finished.emit(False)

    @Slot()
    def _on_installation_requested(self):
        software_row = cast(SoftwareProgressRow, self.sender())

        if self.skip_installation_checkbox.isChecked() or software_row.software.is_archive or not software_row.download_file or not software_row.download_file.exists():
            software_row.finished.emit(SoftwareProgressRow.OperationError.NoError)
            return

        self.pending_installations.append(software_row)
        self._start_next_installation()

    def _start_next_installation(self):
        if self.active_installation is None and len(self.pending_installations) > 0:
            try:
                software_row = self.pending_installations.popleft()
                self.active_installation = software_row
                software_row.start_installation()
            except IndexError:
                pass

    @Slot(SoftwareProgressRow.OperationError)
    def _on_software_row_finished(self, error: SoftwareProgressRow.OperationError):
        software_row = cast(SoftwareProgressRow, self.sender())
        if error != SoftwareProgressRow.OperationError.NoError:
            self.errored_software.append(software_row.software)
        else:
            self.downloaded_software.append(software_row.software)
            software_row.deleteLater()

        if len(self.software_rows) == 0:
            self.cancel_button.setText('&Finish')

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
                self.finished.emit(True)
        else:
            self._start_next_downloads()

        self.active_installation = None
    #endregion

    #region UI Setup
    def _create_layout(self):
        # Main horizontal layout
        self.main_layout = QHBoxLayout()

        # Left side: vertical layout for progress display and buttons
        left_layout = QVBoxLayout()
        left_layout.addWidget(self._create_software_progress_display())
        left_layout.addWidget(self._create_buttons())

        # Add left layout and controls to the main layout
        self.main_layout.addLayout(left_layout, stretch=1)
        self.main_layout.addWidget(self._create_controls())

        return self.main_layout

    def _create_controls(self):
        self.controls_widget = QWidget()
        self.controls_layout = QVBoxLayout(self.controls_widget)
        # self.controls_layout.setContentsMargins(0, 6, 0, 6)

        self.skip_installation_checkbox = QCheckBox('Skip installation (download only)')
        self.skip_installation_checkbox.checkStateChanged.connect(self._on_options_check_state_changed)

        self.silent_install_checkbox = QCheckBox('Try to install silently')
        self.silent_install_checkbox.checkStateChanged.connect(self._on_options_check_state_changed)

        self.postinstall_cleanup_checkbox = QCheckBox('Delete executables after installation')
        self.postinstall_cleanup_checkbox.checkStateChanged.connect(self._on_options_check_state_changed)

        self.postinstall_open_dir_checkbox = QCheckBox('Show downloaded files when finished')
        self.postinstall_open_dir_checkbox.checkStateChanged.connect(self._on_options_check_state_changed)

        self.post_op_row = QHBoxLayout()
        self.post_op_label = QLabel('When done:')
        self.post_op_label.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.post_op_combobox = QComboBox()
        self.post_op_combobox.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        self.post_op_combobox.addItem('Do nothing', PostOperationAction.DoNothing)
        self.post_op_combobox.addItem('Quit', PostOperationAction.CloseApp)
        self.post_op_combobox.addItem('Log Out', PostOperationAction.LogOut)
        self.post_op_combobox.addItem('Lock system', PostOperationAction.Lock)
        self.post_op_combobox.addItem('Restart', PostOperationAction.Restart)
        self.post_op_combobox.addItem('Shut down system', PostOperationAction.ShutDown)
        self.post_op_combobox.setCurrentIndex(0)
        self.post_op_row.addWidget(self.post_op_label)
        self.post_op_row.addWidget(self.post_op_combobox)
        self.post_op_row.addStretch()

        self.controls_layout.addWidget(self.skip_installation_checkbox)
        self.controls_layout.addWidget(self.silent_install_checkbox)
        self.controls_layout.addWidget(self.postinstall_cleanup_checkbox)
        self.controls_layout.addWidget(self.postinstall_open_dir_checkbox)
        self.controls_layout.addLayout(self.post_op_row)
        self.controls_layout.addStretch()

        return self.controls_widget

    def _create_software_progress_display(self):
        self.software_progress_container = QScrollArea()
        self.software_progress_container.setWidgetResizable(True)
        if self.style().name() == 'fusion' or self.style().name() == 'windows':
            self.software_progress_container.setStyleSheet(f'''
                QScrollArea {{ background: {self.palette().color(self.backgroundRole()).lighter(150).name()}; border: 1px solid {ThemeUtil.get_accent_color_name()}; }}
                QScrollArea > QWidget > QWidget {{ background: transparent; }}
                QScrollArea > QWidget > QScrollBar {{ background: 1; }}
            ''')
        else:
            self.software_progress_container.setStyleSheet(f'''
                QScrollArea {{ background: #fff; border: 1px solid {ThemeUtil.get_accent_color_name()}; }}
                QScrollArea > QWidget > QWidget {{ background: transparent; }}
                QScrollArea > QWidget > QScrollBar {{ background: 1; }}
            ''')

        self.software_progress_widget = QWidget()

        self.software_progress_layout = QVBoxLayout(self.software_progress_widget)
        self.software_progress_layout.setSpacing(0)
        self.software_progress_layout.setContentsMargins(0, 0, 0, 0)
        self.software_progress_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.software_progress_widget.setLayout(self.software_progress_layout)
        self.software_progress_container.setWidget(self.software_progress_widget)

        return self.software_progress_container

    def _create_buttons(self):
        self.buttons_widget = QWidget()
        self.buttons_layout = QHBoxLayout(self.buttons_widget)
        self.buttons_layout.setContentsMargins(0, 0, 0, 0)

        self.start_button = QPushButton('&Start')
        self.start_button.setFixedHeight(32)
        self.start_button.clicked.connect(self._on_start_button_clicked)

        self.cancel_button = QPushButton('&Cancel')
        self.cancel_button.setFixedHeight(32)
        self.cancel_button.clicked.connect(self._on_cancel_button_clicked)

        self.buttons_layout.addWidget(self.start_button)
        self.buttons_layout.addWidget(self.cancel_button)
        self.buttons_layout.addStretch()
        self.buttons_widget.setLayout(self.buttons_layout)

        return self.buttons_widget
    #endregion

    def _start_next_downloads(self):
        try:
            software_row = self.software_rows.popleft()
            software_row.start_download(
                self.skip_installation_checkbox.isChecked(),
                self.silent_install_checkbox.isChecked(),
                self.postinstall_cleanup_checkbox.isChecked(),
            )
        except IndexError:
            pass
