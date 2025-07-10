from enum import IntEnum

class DownloadTimeout(IntEnum):
    ThreeMinutes = 1_000 * 60 * 3
    FiveMinutes = 1_000 * 60 * 5
    TenMinutes = 1_000 * 60 * 10
    ThirtyMinutes = 1_000 * 60 * 30
