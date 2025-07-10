from enum import Enum
from pickle import dumps, loads
from src import SETTINGS_FILE_PATH
from PySide6.QtCore import Signal, QObject
from typing import Any, cast, Self, Type, TypeVar, Optional

_T = TypeVar('_T')

class Settings(QObject):
    saved = Signal()

    _initialized = False
    _instance = cast(Optional[Self], None)
    _settings = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        super().__init__()

        self._initialized = True

    def load(self):
        if not SETTINGS_FILE_PATH.exists():
            SETTINGS_FILE_PATH.parent.mkdir(parents=True, exist_ok=True)
            SETTINGS_FILE_PATH.touch()
        else:
            with open(SETTINGS_FILE_PATH, 'rb') as f:
                self._settings = loads(f.read())

    def get(self, key: str, default: _T = None, type_: Type[_T] = None) -> _T:
        value = self._settings.get(key, default)
        if type_ is not None and value is not None:
            try:
                return type_(value)
            except (TypeError, ValueError):
                return default

        return value

    def set(self, key: str, value: Any):
        if isinstance(key, Enum):
            key = key.value

        self._settings[key] = value

    def save(self):
        with open(SETTINGS_FILE_PATH, 'wb') as f:
            f.write(dumps(self._settings))
            self.saved.emit()
