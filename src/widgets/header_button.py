from typing import Optional
from PySide6.QtGui import QPixmap
from src.lib.theme import ThemeUtil
from PySide6.QtCore import Qt, Signal, QObject
from PySide6.QtWidgets import QLabel, QGraphicsOpacityEffect

class HeaderButton(QLabel):
    clicked = Signal()

    def __init__(self, icon: str, tooltip: str, parent: Optional[QObject] = None):
        super().__init__(parent)

        self._hovered = False
        self._clicked = False

        self._initial_opacity = 0.80
        self._hovered_opacity = 1
        self._disabled_opacity = 0.50

        self.opacity_effect = QGraphicsOpacityEffect(self)
        self.opacity_effect.setOpacity(self._initial_opacity)
        self.opacity_effect.setEnabled(True)

        if ThemeUtil.should_use_dark_colors():
            self.pixmap = QPixmap(f':images/{icon}_white.png')
        else:
            self.pixmap = QPixmap(f':images/{icon}.png')
        self.scaled_pixmap = self.pixmap.scaled(22, 22, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)

        self.setGraphicsEffect(self.opacity_effect)
        self.setToolTip(tooltip)
        self.setMouseTracking(True)
        self.setPixmap(self.scaled_pixmap)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFixedSize(45, 48)

    #region Overrides
    def enterEvent(self, event):
        self._hovered = True
        if self.isEnabled():
            self.opacity_effect.setOpacity(self._hovered_opacity)

    def leaveEvent(self, event):
        self._hovered = False
        if self.isEnabled():
            self.opacity_effect.setOpacity(self._initial_opacity)

    def mousePressEvent(self, event):
        self._clicked = True

    def mouseReleaseEvent(self, event):
        self._clicked = False

        if self.rect().contains(event.pos()):
            self.clicked.emit()

    def setEnabled(self, enabled: bool):
        super().setEnabled(enabled)

        if enabled:
            self.opacity_effect.setOpacity(self._initial_opacity)
        else:
            self.opacity_effect.setOpacity(self._disabled_opacity)

    def setDisabled(self, disabled: bool):
        super().setDisabled(disabled)

        if disabled:
            self.opacity_effect.setOpacity(self._disabled_opacity)
        else:
            self.opacity_effect.setOpacity(self._initial_opacity)
    #endregion
