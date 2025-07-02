from pathlib import Path
from enum import auto, Enum
from functools import cache
from typing import List, Optional
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QFontDatabase
from PySide6.QtCore import Qt, QTimer, QObject

BOOT_FONT_PATH = r'C:\Windows\Boot\Fonts_EX\segoe_slboot_EX.ttf'

class Spinner(QLabel):
    class SpinnerStyle(Enum):
        Dots = auto()
        Solid = auto()

    _style: SpinnerStyle
    _characters: List[str] = []
    _timer: QTimer
    _spinning = False
    _current_index = 0

    def __init__(self, style: Optional[SpinnerStyle] = SpinnerStyle.Dots, parent: Optional[QObject] = None):
        super().__init__(parent)

        self._style = style
        self._characters = self._get_char_sequence(0xE052, 0xE0CB) if style == Spinner.SpinnerStyle.Dots else self._get_char_sequence(0xE100, 0xE176)
        self._timer = QTimer()
        self._timer.setInterval(18)
        self._timer.timeout.connect(self._update_spinner_characters)

        if not Path(BOOT_FONT_PATH).exists():
            raise Exception('Could not load system boot font')

        QFontDatabase.addApplicationFont(BOOT_FONT_PATH)

        self.setFont('Segoe Boot Semilight')
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._reset()

    def start(self):
        if not self._spinning:
            self._timer.start()
            self._spinning = True

    def stop(self):
        if self._spinning:
            self._timer.stop()
            self._spinning = False
            self._reset()

    def _update_spinner_characters(self):
        self._current_index = (self._current_index + 1) % len(self._characters)
        self.setText(self._characters[self._current_index])

    def _reset(self):
        if self._style == Spinner.SpinnerStyle.Solid:
            self.setText('')
        else:
            self.setText(self._characters[0])

    @cache
    def _get_char_sequence(self, start: int, end: int) -> List[str]:
        if start >= end:
            raise ValueError('Start of the range must be less than the end.')

        return [chr(start + i) for i in range(end - start)]
