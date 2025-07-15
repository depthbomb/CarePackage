from src import IS_COMPILED
from typing import cast, Optional
from src import SOFTWARE_CATALOGUE
from src.lib.theme import ThemeUtil
from src.lib.settings import Settings
from PySide6.QtCore import Slot, QObject, QThread
from src.lib.download_sweeper import DownloadSweeperWorker
from src.enums import AppStyle, AppTheme, SettingsKeys, DownloadTimeout
from PySide6.QtWidgets import (
    QLabel,
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

        # Track "initialization" so the warning label isn't shown until after fields are populated
        self._initialized = False

        self.thread = cast(Optional[QThread], None)
        self.worker = cast(Optional[DownloadSweeperWorker], None)

        self.setWindowTitle('Settings')
        self.setMinimumWidth(360)
        self.setLayout(self._create_layout())
        self.adjustSize()
        self.setFixedSize(self.size())

        settings = Settings()

        self.download_timeout_combobox.setCurrentIndex(
            self.download_timeout_combobox.findData(settings.get(SettingsKeys.DownloadTimeout, DownloadTimeout.FiveMinutes, int))
        )
        self.style_combobox.setCurrentIndex(
            self.style_combobox.findData(settings.get(SettingsKeys.Style, AppStyle.WindowsVista))
        )
        self.theme_combobox.setCurrentIndex(
            self.theme_combobox.findData(settings.get(SettingsKeys.Theme, AppTheme.Light))
        )
        self.badge_visibility_checkbox.setChecked(
            settings.get(SettingsKeys.ShowCategoryBadges, True, bool)
        )

        self._start_sweeper(DownloadSweeperWorker.Mode.Scan)

        self._initialized = True

    #region Overrides
    def showEvent(self, event):
        ThemeUtil.use_immersive_dark_mode(self)
        super().showEvent(event)
    #endregion

    #region Slots
    @Slot(int, int)
    def _on_sweeper_finished_scanning(self, found_files: int, total_size: int):
        if found_files > 0:
            self.sweeper_button.setEnabled(True)
            self.sweeper_button.setText(f'Clean up {self._pluralize('file', found_files)} ({self._bytes_to_human_readable(total_size)})')
        else:
            self.sweeper_button.setText('No files to clean up')

    @Slot(int)
    def _on_style_or_theme_combobox_changed(self):
        if self._initialized:
            self.restart_warning_label.setVisible(True)

    @Slot(int)
    def _on_style_combobox_changed(self, index: int):
        data = self.style_combobox.itemData(index)
        if data != AppStyle.WindowsVista:
            self.theme_combobox.setEnabled(True)
        else:
            self.theme_combobox.setCurrentIndex(self.theme_combobox.findData(AppTheme.Light))
            self.theme_combobox.setEnabled(False)

    @Slot()
    def _on_sweeper_button_clicked(self):
        self.save_button.setEnabled(False)
        self.sweeper_button.setEnabled(False)
        self.sweeper_button.setText('Cleaning up files...')

        self._start_sweeper(DownloadSweeperWorker.Mode.CleanUp)

    @Slot()
    def _on_clear_url_cache_button_clicked(self):
        self.clear_cache_button.setEnabled(False)
        for software in SOFTWARE_CATALOGUE:
            software.cached_url = None

        self.clear_cache_button.setEnabled(True)

    @Slot(int, int)
    def _on_sweeper_finished_sweeping(self, found_files: int, total_size: int):
        if found_files > 0:
            self.sweeper_button.setText('No files to clean up')

            mb = QMessageBox(self)
            mb.setWindowTitle('Cleanup Complete')
            mb.setIcon(QMessageBox.Icon.Information)
            mb.setText(f'Cleaned up {self._pluralize('file', found_files)} totalling {self._bytes_to_human_readable(total_size)}!')
            mb.exec()

        self.save_button.setEnabled(True)

    @Slot()
    def _on_save_button_clicked(self):
        settings = Settings()
        settings.set(SettingsKeys.DownloadTimeout, self.download_timeout_combobox.currentData())
        settings.set(SettingsKeys.Style, self.style_combobox.currentData())
        settings.set(SettingsKeys.Theme, self.theme_combobox.currentData())
        settings.set(SettingsKeys.ShowCategoryBadges, self.badge_visibility_checkbox.isChecked())
        settings.save()
        self.accept()
    #endregion

    #region UI Setup
    def _create_layout(self):
        self.layout = QFormLayout(self)
        self.layout.addRow('Download timeout', self._create_download_timeout_row())
        self.layout.addRow('App Style', self._create_style_row())
        self.layout.addRow('App Theme', self._create_theme_row())
        self.layout.addRow('', self._create_badge_visibility_checkbox())
        self.layout.addRow('', self._create_sweeper_button())

        if not IS_COMPILED:
            self.layout.addRow('', self._create_clear_url_cache_button())

        self.layout.addRow(self._create_footer_row())

        return self.layout

    def _create_download_timeout_row(self):
        self.download_timeout_combobox = QComboBox(self)
        self.download_timeout_combobox.addItem('3 minutes', DownloadTimeout.ThreeMinutes.value)
        self.download_timeout_combobox.addItem('5 minutes', DownloadTimeout.FiveMinutes.value)
        self.download_timeout_combobox.addItem('10 minutes', DownloadTimeout.TenMinutes.value)
        self.download_timeout_combobox.addItem('30 minutes', DownloadTimeout.ThirtyMinutes.value)

        return self.download_timeout_combobox

    def _create_style_row(self):
        self.style_combobox = QComboBox(self)
        self.style_combobox.addItem('Native (default)', AppStyle.WindowsVista)
        self.style_combobox.addItem('Fusion', AppStyle.Fusion)
        self.style_combobox.addItem('Windows (old)', AppStyle.Windows)
        self.style_combobox.currentIndexChanged.connect(self._on_style_or_theme_combobox_changed)
        self.style_combobox.currentIndexChanged.connect(self._on_style_combobox_changed)

        return self.style_combobox

    def _create_theme_row(self):
        self.theme_combobox = QComboBox(self)
        self.theme_combobox.setEnabled(False)
        self.theme_combobox.addItem('Light (default)', AppTheme.Light)
        self.theme_combobox.addItem('Dark', AppTheme.Dark)
        self.theme_combobox.addItem('System', AppTheme.Auto)
        self.theme_combobox.currentIndexChanged.connect(self._on_style_or_theme_combobox_changed)

        return self.theme_combobox

    def _create_badge_visibility_checkbox(self):
        self.badge_visibility_checkbox = QCheckBox('Show category badges', self)

        return self.badge_visibility_checkbox

    def _create_software_count_row(self):
        self.show_software_count_checkbox = QCheckBox('Show software count per category', self)

        return self.show_software_count_checkbox

    def _create_sweeper_button(self):
        self.sweeper_button = QPushButton('Scanning...', self)
        self.sweeper_button.setEnabled(False)
        self.sweeper_button.clicked.connect(self._on_sweeper_button_clicked)

        return self.sweeper_button

    def _create_clear_url_cache_button(self):
        self.clear_cache_button = QPushButton('Clear resolved URL cache (debug)', self)
        self.clear_cache_button.clicked.connect(self._on_clear_url_cache_button_clicked)

        return self.clear_cache_button

    def _create_footer_row(self):
        widget = QWidget(self)
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)

        self.restart_warning_label = QLabel('Restart required to apply theme changes')
        self.restart_warning_label.setVisible(False)
        self.restart_warning_label.setStyleSheet('color: orangered;')

        self.save_button = QPushButton('&Save', self)
        self.save_button.clicked.connect(self._on_save_button_clicked)

        layout.addWidget(self.restart_warning_label)
        layout.addStretch()
        layout.addWidget(self.save_button)

        widget.setLayout(layout)

        return widget
    #endregion

    def _start_sweeper(self, mode: DownloadSweeperWorker.Mode):
        self.thread = QThread()
        self.worker = DownloadSweeperWorker(mode)

        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)

        if mode == DownloadSweeperWorker.Mode.Scan:
            self.worker.finished_scanning.connect(self._on_sweeper_finished_scanning)
        else:
            self.worker.finished_sweeping.connect(self._on_sweeper_finished_sweeping)

        self.worker.finished_scanning.connect(self.thread.quit)
        self.worker.finished_sweeping.connect(self.thread.quit)
        self.thread.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.thread.start()

    def _bytes_to_human_readable(self, bytes_: int):
        units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB']
        size = float(bytes_)
        for unit in units:
            if size < 1024:
                return f'{size:.2f}{unit}'

            size /= 1024

        return f'{size:.2f}ZB'

    def _pluralize(self, word: str, num: int):
        if num == 1:
            return f'{num} {word}'
        else:
            if word.endswith('y') and word[-2] not in 'aeiou':
                plural = word[:-1] + 'ies'
            elif word.endswith(('s', 'sh', 'ch', 'x', 'z')):
                plural = word + 'es'
            else:
                plural = word + 's'

            return f'{num} {plural}'
