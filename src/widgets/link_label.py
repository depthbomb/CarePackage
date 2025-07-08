from typing import Optional
from src.lib.theme import ThemeUtil
from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt, Signal, QObject

class LinkLabel(QLabel):
    clicked = Signal()

    def __init__(self, text: str, parent: Optional[QObject] = None):
        super().__init__(parent)

        self._hovered = False
        self._clicked = False

        self._initial_color = ThemeUtil.get_accent_color_shade(ThemeUtil.Mode.Darker, 150).name()
        self._hovered_color = ThemeUtil.get_accent_color_shade(ThemeUtil.Mode.Darker, 200).name()
        self._clicked_color = ThemeUtil.get_accent_color_shade(ThemeUtil.Mode.Darker, 300).name()

        self.setText(text)
        self.setMouseTracking(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self._apply_styles()

    #region Overrides
    def enterEvent(self, event):
        self._hovered = True
        self._apply_styles()

    def leaveEvent(self, event):
        self._hovered = False
        self._apply_styles()

    def mousePressEvent(self, event):
        self._clicked = True
        self._apply_styles()

    def mouseReleaseEvent(self, event):
        self._clicked = False

        if self.rect().contains(event.pos()):
            self.clicked.emit()

        self._apply_styles()

    def setEnabled(self, enabled: bool):
        if enabled:
            self.setCursor(Qt.CursorShape.PointingHandCursor)
        else:
            self.setCursor(Qt.CursorShape.ForbiddenCursor)

        super().setEnabled(enabled)

        self._apply_styles()

    def setDisabled(self, disabled: bool):
        if disabled:
            self.setCursor(Qt.CursorShape.ForbiddenCursor)
        else:
            self.setCursor(Qt.CursorShape.PointingHandCursor)

        super().setDisabled(disabled)

        self._apply_styles()
    #endregion

    def _apply_styles(self):
        if not self.isEnabled():
            self.setStyleSheet('')
            return

        if self._clicked:
            self.setStyleSheet(f'QLabel {{ color: {self._clicked_color} }}')
        elif self._hovered:
            self.setStyleSheet(f'QLabel {{ color: {self._hovered_color} }}')
        else:
            self.setStyleSheet(f'QLabel {{ color: {self._initial_color} }}')
