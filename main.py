from sys import argv, exit
from PySide6.QtCore import Qt
from src.lib.settings import Settings
from src.windows.main_window import MainWindow
from src import APP_ORG, APP_NAME, APP_VERSION_STRING
from src.enums import AppStyle, AppTheme, SettingsKeys
from PySide6.QtWidgets import QMessageBox, QApplication
from src.windows.disclaimer_window import DisclaimerWindow

def main(args) -> int:
    app = QApplication(args)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION_STRING)
    app.setOrganizationName(APP_ORG)

    settings = Settings()
    settings.load()

    if not settings.get(SettingsKeys.SeenDisclaimer, False, bool):
        if DisclaimerWindow().exec() != QMessageBox.StandardButton.Yes:
            return 0
        else:
            settings.set(SettingsKeys.SeenDisclaimer, True)
            settings.save()

    user_style = settings.get(SettingsKeys.Style, AppStyle.WindowsVista, AppStyle)
    if user_style != AppStyle.WindowsVista:
        user_theme = settings.get(SettingsKeys.Theme, AppTheme.Light, AppTheme)
        if user_theme == AppTheme.Dark:
            app.styleHints().setColorScheme(Qt.ColorScheme.Dark)
        else:
            app.styleHints().setColorScheme(Qt.ColorScheme.Light)

    app.setStyle(user_style)

    w = MainWindow()
    w.show()

    return app.exec()

if __name__ == '__main__':
    exit(main(argv))
