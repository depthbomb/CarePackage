from sys import argv, exit
from PySide6.QtWidgets import QApplication
from src.windows.main_window import MainWindow
from src import APP_ORG, APP_NAME, APP_VERSION_STRING
from src.lib.settings import app_settings, AppSettingsKeys
from src.windows.disclaimer_window import DisclaimerWindow

def main(args) -> int:
    app = QApplication(args)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION_STRING)
    app.setOrganizationName(APP_ORG)

    if not bool(app_settings.value(AppSettingsKeys.SeenDisclaimer, False, bool)):
        if DisclaimerWindow().exec() != 2:
            return 0
        else:
            app_settings.setValue(AppSettingsKeys.SeenDisclaimer, True)

    w = MainWindow()
    w.show()

    return app.exec()

if __name__ == '__main__':
    exit(main(argv))
