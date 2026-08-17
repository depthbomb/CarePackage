from enum import IntEnum

class DownloadTimeout(IntEnum):
    TenSeconds = 1_000 * 10
    ThirtySeconds = 1_000 * 30
    OneMinute = 1_000 * 60
    ThreeMinutes = 1_000 * 60 * 3
    FiveMinutes = 1_000 * 60 * 5
    TenMinutes = 1_000 * 60 * 10
    ThirtyMinutes = 1_000 * 60 * 30
