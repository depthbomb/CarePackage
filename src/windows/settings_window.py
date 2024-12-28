from typing import cast, Optional
from PySide6.QtCore import Slot, QObject
from src.lib.download_sweeper import DownloadSweeper
from src.lib.settings import user_settings, DownloadTimeout, UserSettingsKeys
from PySide6.QtWidgets import (
    QWidget,
    QDialog,
    QComboBox,
    QCheckBox,
    QMessageBox,
    QPushButton,
    QFormLayout,
    QHBoxLayout,
)

class SettingsWindow(QDialog):
    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)

        self.sweeper = cast(Optional[DownloadSweeper], DownloadSweeper(DownloadSweeper.Mode.Scan, None))
        self.sweeper.finished_scanning.connect(self._on_sweeper_finished_scanning)
        self.sweeper.start()

        self.setLayout(self._create_layout())
        self.setMinimumWidth(360)
        self.adjustSize()
        self.setFixedSize(self.size())

        self.theme_combobox.setCurrentIndex(
            self.theme_combobox.findData(user_settings.value(UserSettingsKeys.Theme))
        )
        self.download_timeout_combobox.setCurrentIndex(
            self.download_timeout_combobox.findData(user_settings.value(UserSettingsKeys.DownloadTimeout, 0, int))
        )
        self.sweep_on_close_checkbox.setChecked(
            user_settings.value(UserSettingsKeys.SweepFilesOnClose, False, bool)
        )
        self.show_software_count_checkbox.setChecked(
            user_settings.value(UserSettingsKeys.ShowCategorySoftwareCount, False, bool)
        )

    #region Slots
    @Slot(int)
    def _on_sweeper_finished_scanning(self, found_files: int):
        if found_files > 0:
            self.sweeper_button.setEnabled(True)

        self.sweeper.deleteLater()
        self.sweeper = None

    @Slot()
    def _on_sweeper_button_clicked(self):
        self.save_button.setEnabled(False)
        self.sweeper_button.setEnabled(False)

        self.sweeper = DownloadSweeper(DownloadSweeper.Mode.CleanUp, self)
        self.sweeper.finished_sweeping.connect(self._on_sweeper_finished_sweeping)
        self.sweeper.start()

    @Slot(int)
    def _on_sweeper_finished_sweeping(self, found_files: int):
        if found_files > 0:
            mb = QMessageBox(self)
            mb.setWindowTitle('Cleanup Complete')
            mb.setIcon(QMessageBox.Icon.Information)
            mb.setText(f'Cleaned up {found_files} file(s)!')
            mb.exec()

        self.save_button.setEnabled(True)

        self.sweeper.deleteLater()
        self.sweeper = None

    @Slot()
    def _on_save_button_clicked(self):
        user_settings.setValue(UserSettingsKeys.Theme, self.theme_combobox.currentData())
        user_settings.setValue(UserSettingsKeys.DownloadTimeout, self.download_timeout_combobox.currentData())
        user_settings.setValue(UserSettingsKeys.SweepFilesOnClose, self.sweep_on_close_checkbox.isChecked())
        user_settings.setValue(UserSettingsKeys.ShowCategorySoftwareCount, self.show_software_count_checkbox.isChecked())
        self.accept()
    #endregion

    def _create_layout(self):
        self.layout = QFormLayout(self)
        self.layout.addRow('Theme', self._create_theme_row())
        self.layout.addRow('Download timeout', self._create_download_timeout_row())
        self.layout.addRow('', self._create_sweep_on_close_row())
        self.layout.addRow('', self._create_software_count_row())
        self.layout.addRow('', self._create_sweeper_button())
        self.layout.addWidget(self._create_footer_row())

        return self.layout

    def _create_theme_row(self):
        self.theme_combobox = QComboBox(self)
        self.theme_combobox.addItem('Fusion Light (default)', True)
        self.theme_combobox.addItem('Native', False)

        return self.theme_combobox

    def _create_download_timeout_row(self):
        self.download_timeout_combobox = QComboBox(self)
        self.download_timeout_combobox.addItem('3 minutes', DownloadTimeout.ThreeMinutes.value)
        self.download_timeout_combobox.addItem('5 minutes', DownloadTimeout.FiveMinutes.value)
        self.download_timeout_combobox.addItem('10 minutes', DownloadTimeout.TenMinutes.value)
        self.download_timeout_combobox.addItem('30 minutes', DownloadTimeout.ThirtyMinutes.value)

        return self.download_timeout_combobox

    def _create_sweep_on_close_row(self):
        self.sweep_on_close_checkbox = QCheckBox('Delete downloaded files on quit', self)

        return self.sweep_on_close_checkbox

    def _create_software_count_row(self):
        self.show_software_count_checkbox = QCheckBox('Show software count per category', self)

        return self.show_software_count_checkbox

    def _create_sweeper_button(self):
        self.sweeper_button = QPushButton('&Clean up downloads', self)
        self.sweeper_button.setEnabled(False)
        self.sweeper_button.clicked.connect(self._on_sweeper_button_clicked)

        return self.sweeper_button

    def _create_footer_row(self):
        widget = QWidget(self)
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)

        self.save_button = QPushButton('&Save', self)
        self.save_button.clicked.connect(self._on_save_button_clicked)

        layout.addStretch()
        layout.addWidget(self.save_button)

        widget.setLayout(layout)

        return widget
