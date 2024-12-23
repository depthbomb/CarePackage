from abc import abstractmethod
from typing import cast, Optional
from enum import auto, Enum, StrEnum
from PySide6.QtCore import Slot, Signal, QObject
from PySide6.QtNetwork import QNetworkReply, QNetworkAccessManager

class SoftwareCategory(StrEnum):
    Browser = 'Web Browsers'
    Gaming = 'Gaming'
    Social = 'Social'
    Media = 'Media'
    Utility = 'Utilities'
    DotNet = '.NET'
    Runtime = 'Runtimes'
    Peripheral = 'Peripherals'
    Development = 'Development'
    Creative = 'Creative Tools'
    Security = 'Security'

class BaseSoftware(QObject):
    class ResolveError(Enum):
        URLResolveError = auto()
        GitHubAssetNotFoundError = auto()

    url_resolved = Signal(str)
    url_resolve_error = Signal(ResolveError)

    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)

        self.manager = QNetworkAccessManager(self)
        self.manager.setTransferTimeout(5_000)
        self.manager.finished.connect(self.on_manager_finished)

        self.cached_url = cast(Optional[str], None)

        self._key = cast(Optional[str], None)
        self._name = cast(Optional[str], None)
        self._category = cast(Optional[SoftwareCategory], None)
        self._download_name = cast(Optional[str], None)
        self._is_archive = cast(Optional[bool], None)
        self._should_cache_url = cast(Optional[bool], None)
        self._requires_admin = cast(Optional[bool], None)
        self._icon = cast(Optional[str], None)
        self._homepage = cast(Optional[str], None)

    #region Properties
    @property
    @abstractmethod
    def key(self) -> str:
        return self._key

    @key.setter
    @abstractmethod
    def key(self, key: str):
        self._key = key

    @property
    @abstractmethod
    def name(self) -> str:
        return self._name

    @name.setter
    @abstractmethod
    def name(self, name: str):
        self._name = name

    @property
    @abstractmethod
    def category(self) -> SoftwareCategory:
        return self._category

    @category.setter
    @abstractmethod
    def category(self, category: SoftwareCategory):
        self._category = category

    @property
    @abstractmethod
    def download_name(self) -> str:
        return self._download_name

    @download_name.setter
    @abstractmethod
    def download_name(self, download_name: str):
        self._download_name = download_name

    @property
    @abstractmethod
    def is_archive(self) -> bool:
        return self._is_archive

    @is_archive.setter
    @abstractmethod
    def is_archive(self, is_archive: bool):
        self._is_archive = is_archive

    @property
    @abstractmethod
    def should_cache_url(self) -> bool:
        return self._should_cache_url

    @should_cache_url.setter
    @abstractmethod
    def should_cache_url(self, should_cache_url: bool):
        self._should_cache_url = should_cache_url

    @property
    @abstractmethod
    def requires_admin(self) -> bool:
        return self._requires_admin

    @requires_admin.setter
    @abstractmethod
    def requires_admin(self, requires_admin: bool):
        self._requires_admin = requires_admin

    @property
    @abstractmethod
    def icon(self) -> str:
        return self._icon

    @icon.setter
    @abstractmethod
    def icon(self, icon: str):
        self._icon = icon

    @property
    @abstractmethod
    def homepage(self) -> str:
        return self._homepage

    @homepage.setter
    @abstractmethod
    def homepage(self, homepage: str):
        self._homepage = homepage
    #endregion

    #region Methods
    @abstractmethod
    def resolve_download_url(self):
        pass

    @abstractmethod
    @Slot(QNetworkReply)
    def on_manager_finished(self, reply: QNetworkReply):
        pass
    #endregion