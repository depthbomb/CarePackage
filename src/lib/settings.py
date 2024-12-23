from PySide6.QtCore import QSettings
from enum import auto, IntEnum, StrEnum
from src import APP_SETTINGS_FILE_PATH, USER_SETTINGS_FILE_PATH

class DownloadTimeout(IntEnum):
    ThreeMinutes = 1_000 * 60 * 3
    FiveMinutes = 1_000 * 60 * 5
    TenMinutes = 1_000 * 60 * 10
    ThirtyMinutes = 1_000 * 60 * 30

class PostOperationAction(IntEnum):
    DoNothing = auto()
    CloseApp = auto()
    LogOut = auto()
    Lock = auto()
    Restart = auto()
    ShutDown = auto()

app_settings = QSettings(str(APP_SETTINGS_FILE_PATH), QSettings.Format.IniFormat)
user_settings = QSettings(str(USER_SETTINGS_FILE_PATH), QSettings.Format.IniFormat)

class AppSettingsKeys(StrEnum):
    SeenDisclaimer = 'app/seen_disclaimer'

class UserSettingsKeys(StrEnum):
    Theme = 'app/theme'
    DownloadTimeout = 'user/download_timeout'
    DownloadDir = 'user/download_dir'
    ShowCategorySoftwareCount = 'user/show_category_software_count'
