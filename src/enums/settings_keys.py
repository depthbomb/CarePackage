from enum import StrEnum

class SettingsKeys(StrEnum):
    SeenDisclaimer = 'app/seen_disclaimer'
    #
    DownloadTimeout = 'user/download_timeout'
    DownloadDir = 'user/download_dir'
    ShowCategoryBadges = 'user/show_category_badges'
    Style = 'user/style'
    Theme = 'user/theme'
