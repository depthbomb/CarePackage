from sys import argv, exit
from PySide6.QtCore import Qt
from src.windows.main_window import MainWindow
from src import APP_ORG, APP_NAME, APP_VERSION_STRING
from PySide6.QtWidgets import QMessageBox, QApplication
from src.lib.settings import app_settings, AppSettingsKeys
from src.windows.disclaimer_window import DisclaimerWindow
from src.lib.settings import AppStyle, AppTheme, user_settings, UserSettingsKeys

def main(args) -> int:
    app = QApplication(args)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION_STRING)
    app.setOrganizationName(APP_ORG)

    if not bool(app_settings.value(AppSettingsKeys.SeenDisclaimer, False, bool)):
        if DisclaimerWindow().exec() != QMessageBox.StandardButton.Yes:
            return 0
        else:
            app_settings.setValue(AppSettingsKeys.SeenDisclaimer, True)

    user_style = user_settings.value(UserSettingsKeys.Style, AppStyle.WindowsVista)
    if user_style != AppStyle.WindowsVista:
        user_theme = user_settings.value(UserSettingsKeys.Theme, AppTheme.Light)
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
