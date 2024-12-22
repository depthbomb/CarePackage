from enum import auto, Enum
from typing import Optional
from src import ALL_SOFTWARE, DOWNLOAD_DIR
from PySide6.QtCore import QFile, Signal, QObject, QThread

class DownloadSweeper(QThread):
    class Mode(Enum):
        Scan = auto()
        CleanUp = auto()

    finished_scanning = Signal(int)
    sweeping_files = Signal()
    finished_sweeping = Signal(int)

    def __init__(self, mode: Mode, parent: Optional[QObject] = None):
        super().__init__(parent)

        self.mode = mode

    def run(self):
        found_files = 0

        if self.mode == self.Mode.Scan:
            for software in ALL_SOFTWARE:
                sw = software()
                file_path = QFile(DOWNLOAD_DIR / sw.download_name)
                del sw
                if file_path.exists():
                    found_files += 1

            self.finished_scanning.emit(found_files)
        else:
            self.sweeping_files.emit()

            for software in ALL_SOFTWARE:
                sw = software()
                file_path = QFile(DOWNLOAD_DIR / sw.download_name)
                del sw
                if file_path.exists():
                    file_path.remove()
                    found_files += 1

            self.finished_sweeping.emit(found_files)
