from typing import Optional
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Signal, QTimer, QObject

class LoadingLabel(QLabel):
    animation_state_changed = Signal(bool)

    def __init__(self, text='', parent: Optional[QObject] = None):
        super().__init__(parent)

        self._base_text = text
        self._ellipsis_count = 0
        self._max_ellipsis = 3

        self._timer = QTimer()
        self._timer.timeout.connect(self._update_ellipsis)
        self._animation_speed = 500

        self.setText(self._base_text)

        self._is_animating = False

    def set_base_text(self, text):
        self._base_text = text
        if not self._is_animating:
            self.setText(text)
        else:
            self._update_display()

    def get_base_text(self):
        return self._base_text

    def set_animation_speed(self, milliseconds):
        self._animation_speed = milliseconds
        if self._is_animating:
            self._timer.setInterval(milliseconds)

    def get_animation_speed(self):
        return self._animation_speed

    def set_max_ellipsis(self, count):
        self._max_ellipsis = max(1, count)

    def get_max_ellipsis(self):
        return self._max_ellipsis

    def start_animation(self):
        if not self._is_animating:
            self._is_animating = True
            self._ellipsis_count = 0
            self._timer.start(self._animation_speed)
            self._update_display()
            self.animation_state_changed.emit(True)

    def stop_animation(self):
        if self._is_animating:
            self._is_animating = False
            self._timer.stop()
            self.setText(self._base_text)
            self.animation_state_changed.emit(False)

    def is_animating(self):
        return self._is_animating

    def toggle_animation(self):
        if self._is_animating:
            self.stop_animation()
        else:
            self.start_animation()

    def _update_ellipsis(self):
        self._ellipsis_count = (self._ellipsis_count + 1) % (self._max_ellipsis + 1)
        self._update_display()

    def _update_display(self):
        ellip = '.' * self._ellipsis_count
        display_text = f'{self._base_text}{ellip}'
        self.setText(display_text)
