from sys import argv, exit
from PySide6.QtWidgets import QApplication
from src.windows.main_window import MainWindow
from src.windows.disclaimer_window import DisclaimerWindow
from src import APP_ORG, APP_NAME, IS_ONEFILE, DOWNLOAD_DIR, APP_DISPLAY_NAME, APP_VERSION_STRING
from src.lib.settings import app_settings, user_settings, DownloadTimeout, AppSettingsKeys, UserSettingsKeys

argv += ['-platform', 'windows:darkmode=0']

app = QApplication(argv)
app.setApplicationName(APP_NAME)
app.setApplicationDisplayName(APP_DISPLAY_NAME)
app.setApplicationVersion(APP_VERSION_STRING)
app.setOrganizationName(APP_ORG)

if __name__ == '__main__':
    DOWNLOAD_DIR.mkdir(exist_ok=True)

    if not bool(app_settings.value(AppSettingsKeys.SeenDisclaimer, False, bool)):
        if DisclaimerWindow().exec() != 2:
            exit(0)
        else:
            app_settings.setValue(AppSettingsKeys.SeenDisclaimer, True)

    if not IS_ONEFILE:
        if not user_settings.value(UserSettingsKeys.DownloadTimeout, None, int):
            user_settings.setValue(UserSettingsKeys.DownloadTimeout, DownloadTimeout.FiveMinutes.value)

        if user_settings.value(UserSettingsKeys.Theme, None) is None:
            user_settings.setValue(UserSettingsKeys.Theme, True)

        if user_settings.value(UserSettingsKeys.Theme, None, bool):
            app.setStyle('Fusion')
    else:
        app.setStyle('Fusion')

    w = MainWindow()
    w.show()

    exit(app.exec())
