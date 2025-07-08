from typing import Optional
from PySide6.QtGui import QPixmap
from src.lib.theme import ThemeUtil
from PySide6.QtCore import Qt, QObject
from PySide6.QtWidgets import QLabel, QWidget, QHBoxLayout

class Badge(QWidget):
    def __init__(self, text='', icon: Optional[str] = None, parent: Optional[QObject] = None):
        super().__init__(parent)

        self.setObjectName('Badge')

        self.foreground_color = ThemeUtil.get_foreground_color()
        self.background_color = ThemeUtil.get_accent_color_name()

        self.layout = QHBoxLayout(self)
        self.layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        if icon is not None:
            self.layout.setSpacing(4)
            self.pixmap = QPixmap(f':images/{icon}_white.png')
            self.scaled_pixmap = self.pixmap.scaled(14, 14, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            self.image = QLabel(self)
            self.image.setPixmap(self.scaled_pixmap)
            self.image.setFixedSize(14, 14)
            self.layout.addWidget(self.image)
        else:
            self.layout.setSpacing(0)

        self.label = QLabel(text, self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label)

        self.setMinimumWidth(48)
        self.setMinimumHeight(28)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(f'''
            Badge {{
                padding-left: 8px;
                padding-right: 8px;
                background-color: {self.background_color};
                border-radius: 14px;
            }}
            
            Badge QLabel {{
                font-size: 10px;
                font-weight: bold;
                color: {self.foreground_color};
            }}
        ''')
        self.setLayout(self.layout)
