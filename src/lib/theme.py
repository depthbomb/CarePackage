from src.lib import win32
from enum import auto, Enum
from typing import Optional
from functools import cache
from PySide6.QtGui import QColor
from winreg import OpenKey, CloseKey, QueryValueEx, HKEY_CURRENT_USER


class ThemeUtil:
    class Mode(Enum):
        Lighter = auto()
        Darker = auto()

    @staticmethod
    @cache
    def get_accent_color() -> Optional[QColor]:
        try:
            key = OpenKey(
                HKEY_CURRENT_USER,
                r"SOFTWARE\Microsoft\Windows\DWM"
            )

            accent_color_value, _ = QueryValueEx(key, "AccentColor")
            CloseKey(key)

            alpha = (accent_color_value >> 24) & 0xFF
            blue = (accent_color_value >> 16) & 0xFF
            green = (accent_color_value >> 8) & 0xFF
            red = accent_color_value & 0xFF

            return QColor(red, green, blue, alpha)
        except:
            return None

    @staticmethod
    @cache
    def get_accent_color_name():
        return ThemeUtil.get_accent_color().name()

    @staticmethod
    @cache
    def get_accent_color_shade(mode: Mode, shade: int) -> QColor:
        accent_color = ThemeUtil.get_accent_color()
        if accent_color is None:
            return QColor('black')

        if mode == ThemeUtil.Mode.Darker:
            return accent_color.darker(shade)

        return accent_color.lighter(shade)

    @staticmethod
    @cache
    def should_use_dark_colors() -> bool:
        accent_color = ThemeUtil.get_accent_color()
        if not accent_color:
            return True

        r = accent_color.red()
        g = accent_color.green()
        b = accent_color.blue()
        brightness = (0.299 * r + 0.587 * g + 0.114 * b)

        return brightness > 186

    @staticmethod
    @cache
    def get_foreground_color() -> QColor:
        return QColor('black') if ThemeUtil.should_use_dark_colors() else QColor('white')

    @staticmethod
    @cache
    def is_dark_mode() -> bool:
        return win32.is_dark_mode()
