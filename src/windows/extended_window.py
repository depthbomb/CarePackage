from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from src.lib.theme import ThemeUtil
from PySide6.QtWidgets import QWidget, QVBoxLayout, QMainWindow
from ctypes import c_int, byref, WinDLL, wintypes, HRESULT, POINTER, Structure

dwmapi = WinDLL('dwmapi')

class MARGINS(Structure):
    _fields_ = [('cxLeftWidth', c_int),
                ('cxRightWidth', c_int),
                ('cyTopHeight', c_int),
                ('cyBottomHeight', c_int)]

DwmExtendFrameIntoClientArea = dwmapi.DwmExtendFrameIntoClientArea
DwmExtendFrameIntoClientArea.argtypes = [wintypes.HWND, POINTER(MARGINS)]
DwmExtendFrameIntoClientArea.restype = HRESULT

class ExtendedWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.extended_height = 48

        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.bg = self.palette().color(self.backgroundRole())

        self._container = QWidget()
        self._layout = QVBoxLayout(self._container)
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.setSpacing(0)

        self._top_widget = QWidget()
        self._top_widget.setFixedHeight(self.extended_height)

        self._central_placeholder = QWidget()

        self._layout.addWidget(self._top_widget)
        self._layout.addWidget(self._central_placeholder)

        super().setCentralWidget(self._container)

    #region Overrides
    def showEvent(self, event):
        self.extend_frame()
        ThemeUtil.use_immersive_dark_mode(self)
        super().showEvent(event)

    def setCentralWidget(self, widget: QWidget):
        if self._central_placeholder:
            self._layout.replaceWidget(self._central_placeholder, widget)
            self._central_placeholder.deleteLater()
            self._central_placeholder = widget
        else:
            self._layout.addWidget(widget)

        widget.setParent(self._container)
    #endregion

    def extend_frame(self):
        hwnd = self.winId()
        margins = MARGINS(0, 0, self.extended_height, 0)
        DwmExtendFrameIntoClientArea(hwnd, byref(margins))

    def set_extended_widget(self, widget: QWidget):
        if self._top_widget:
            self._layout.replaceWidget(self._top_widget, widget)
            self._top_widget.deleteLater()
            self._top_widget = widget

    def paintEvent(self, event):
            painter = QPainter(self)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            painter.fillRect(self.rect().adjusted(0, self.extended_height, 0, 0), self.bg)
            painter.end()
