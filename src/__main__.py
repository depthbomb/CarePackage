from src.lib import win32
from sys import argv, exit
from src.lib.settings import Settings
from PySide6.QtCore import Qt, QSharedMemory
from src.windows.main_window import MainWindow
from src.enums import AppStyle, AppTheme, SettingsKeys
from PySide6.QtWidgets import QMessageBox, QApplication
from src.windows.disclaimer_window import DisclaimerWindow
from src import APP_ORG, APP_NAME, APP_DISPLAY_NAME, APP_USER_MODEL_ID, APP_VERSION_STRING, IS_WINDOWS11

def _apply_appearance(app: QApplication, settings: Settings):
    native_style = AppStyle.Windows11 if IS_WINDOWS11 else AppStyle.WindowsVista
    user_style = settings.get(SettingsKeys.Style, native_style, AppStyle)

    # WindowsVista was the persisted value for the native style before Windows 11 support was added. Treat it as the
    # current native style on Windows 11.
    if IS_WINDOWS11 and user_style == AppStyle.WindowsVista:
        user_style = AppStyle.Windows11

    if user_style != AppStyle.WindowsVista:
        user_theme = settings.get(SettingsKeys.Theme, AppTheme.Light, AppTheme)
        if user_theme == AppTheme.Dark:
            app.styleHints().setColorScheme(Qt.ColorScheme.Dark)
        elif user_theme == AppTheme.Light:
            app.styleHints().setColorScheme(Qt.ColorScheme.Light)

    app.setStyle(user_style)

def main(args) -> int:
    app = QApplication(args)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION_STRING)
    app.setOrganizationName(APP_ORG)

    shared_mem = QSharedMemory(APP_USER_MODEL_ID)
    if not shared_mem.create(1):
        hwnd = win32.find_window(None, APP_DISPLAY_NAME)
        win32.show_window(hwnd, win32.SW_SHOWNORMAL)
        win32.set_foreground_window(hwnd)
        return 0

    settings = Settings()
    settings.load()

    _apply_appearance(app, settings)

    if not settings.get(SettingsKeys.SeenDisclaimer, False, bool):
        if DisclaimerWindow().exec() != QMessageBox.StandardButton.Yes:
            return 0
        else:
            settings.set(SettingsKeys.SeenDisclaimer, True)
            settings.save()

    w = MainWindow()
    w.show()

    retval = app.exec()
    shared_mem.detach()

    return retval

if __name__ == '__main__':
    exit(main(argv))
