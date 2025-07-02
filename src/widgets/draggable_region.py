from ctypes.wintypes import MSG
from PySide6.QtCore import QPoint
from PySide6.QtWidgets import QWidget
from ctypes import cast, c_short, POINTER

WM_NCHITTEST = 0x0084
HTCLIENT = 1
HTCAPTION = 2

class DraggableWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedHeight(48)

    def contains_global_point(self, global_point: QPoint) -> bool:
        local_pos = self.mapFromGlobal(global_point)
        return self.rect().contains(local_pos)

    def handle_native_event(self, eventType, message):
        if eventType == b'windows_generic_MSG':
            msg = cast(int(message), POINTER(MSG)).contents
            if msg.message == WM_NCHITTEST:
                x = c_short(msg.lParam & 0xFFFF).value
                y = c_short((msg.lParam >> 16) & 0xFFFF).value
                global_pos = QPoint(x, y)

                if self.contains_global_point(global_pos):
                    return True, HTCAPTION

                return False, 0

        return False, 0
