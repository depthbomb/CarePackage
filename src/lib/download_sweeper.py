from enum import Enum, auto
from typing import Optional
from src import DOWNLOAD_DIR
from PySide6.QtCore import Slot, Signal, QObject

class DownloadSweeperWorker(QObject):
    finished_scanning = Signal(int)
    sweeping_files = Signal()
    finished_sweeping = Signal(int)

    class Mode(Enum):
        Scan = auto()
        CleanUp = auto()

    def __init__(self, mode: Mode, parent: Optional[QObject] = None):
        super().__init__(parent)
        self.mode = mode

    @Slot()
    def run(self):
        DOWNLOAD_DIR.mkdir(exist_ok=True)

        found_files = 0

        extensions = ['.exe', '.msi', '.zip', '.rar', '.7z']

        if self.mode == self.Mode.Scan:
            for file in DOWNLOAD_DIR.iterdir():
                if file.is_file() and file.suffix in extensions:
                    found_files += 1

            self.finished_scanning.emit(found_files)
        else:
            self.sweeping_files.emit()
            for file in DOWNLOAD_DIR.iterdir():
                if file.is_file() and file.suffix in extensions:
                    file.unlink()
                    found_files += 1

            self.finished_sweeping.emit(found_files)
