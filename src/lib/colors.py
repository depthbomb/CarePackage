from functools import cache
from PySide6.QtGui import QColor
from winrt.windows.ui.viewmanagement import UISettings, UIColorType

_ui_settings = UISettings()
ACCENT_COLOR = _ui_settings.get_color_value(UIColorType.ACCENT)
ACCENT_COLOR_LIGHT1 = _ui_settings.get_color_value(UIColorType.ACCENT_LIGHT1)
ACCENT_COLOR_LIGHT2 = _ui_settings.get_color_value(UIColorType.ACCENT_LIGHT2)
ACCENT_COLOR_LIGHT3 = _ui_settings.get_color_value(UIColorType.ACCENT_LIGHT3)

@cache
def get_accent_color(type_: UIColorType):
    c = _ui_settings.get_color_value(type_)
    color = QColor(c.r, c.g, c.b, c.a)

    return color.name()
