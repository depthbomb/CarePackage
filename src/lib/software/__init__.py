from abc import abstractmethod
from enum import auto, Enum, StrEnum
from typing import cast, Type, Union, Optional
from PySide6.QtCore import Slot, Signal, QObject
from PySide6.QtNetwork import QNetworkReply, QNetworkAccessManager

class SoftwareCategory(StrEnum):
    Audio = 'Audio & Sounds'
    Browser = 'Web Browsers'
    Creative = 'Creative'
    Development = 'Development'
    Emulation = 'Emulation'
    FileManagement = 'File Management'
    GameDevelopment = 'Video Game Development'
    Gaming = 'Gaming'
    Media = 'Media'
    Modelling = '3D Modelling'
    Network = 'Network Tools'
    Peripheral = 'Peripherals'
    Productivity = 'Notes & Productivity'
    Runtime = 'Runtimes'
    Security = 'Security'
    Social = 'Social'
    SystemManagement = 'System Management'
    Utility = 'Utilities'

class BaseSoftware(QObject):
    class ResolveError(Enum):
        URLResolveError = auto()
        GitHubRequestError = auto()
        GitHubAssetNotFoundError = auto()

    url_resolved = Signal(str)
    url_resolve_error = Signal(ResolveError)

    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)

        self.manager = QNetworkAccessManager(self)
        self.manager.setTransferTimeout(5_000)
        self.manager.finished.connect(self.on_manager_finished)

        self.cached_url = cast(Optional[str], None)

        self._key = ''
        self._name = ''
        self._category = cast(list[SoftwareCategory], [])
        self._download_name = ''
        self._is_archive = False
        self._should_cache_url = False
        self._requires_admin = False
        self._deprecated = False
        self._alternative = cast(Optional[Type[BaseSoftware]], None)
        self._variants = cast(list[Type['BaseSoftware']], [])
        self._icon = 'generic.png'
        self._homepage = ''

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
    def category(self) -> list[SoftwareCategory]:
        return self._category

    @category.setter
    @abstractmethod
    def category(self, category: Union[list[SoftwareCategory] | SoftwareCategory]):
        if isinstance(category, list):
            for cat in category:
                self._category.append(cat)
        else:
            self._category.append(category)

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
    def is_deprecated(self) -> bool:
        return self._deprecated

    @is_deprecated.setter
    @abstractmethod
    def is_deprecated(self, is_deprecated: bool):
        self._deprecated = is_deprecated

    @property
    @abstractmethod
    def alternative(self) -> Type['BaseSoftware']:
        return self._alternative

    @alternative.setter
    @abstractmethod
    def alternative(self, alternative: Type['BaseSoftware']):
        self._alternative = alternative

    @property
    @abstractmethod
    def variants(self) -> list['BaseSoftware']:
        return self._variants

    @variants.setter
    @abstractmethod
    def variants(self, variants: list['BaseSoftware']):
        self._variants = variants

    @property
    def has_variants(self) -> bool:
        return len(self.variants) > 0

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
