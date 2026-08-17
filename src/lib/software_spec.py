from typing import cast
from importlib import import_module
from dataclasses import field, dataclass
from src.lib.software import BaseSoftware, SoftwareCategory

_software_instances: dict[tuple[str, str], BaseSoftware] = {}

@dataclass(frozen=True, slots=True)
class SoftwareSpec:
    module: str
    class_name: str
    key: str
    name: str
    category: tuple[SoftwareCategory, ...]
    icon: str
    homepage: str
    is_archive: bool = False
    is_deprecated: bool = False
    is_unreliable: bool = False
    alternative_name: str | None = None
    variants: tuple['SoftwareSpec', ...] = field(default_factory=tuple)

    @property
    def has_variants(self) -> bool:
        return bool(self.variants)

    def get_instance(self) -> BaseSoftware:
        """Import and construct this definition on first use, then reuse it."""
        identity = (self.module, self.class_name)
        instance = _software_instances.get(identity)
        if instance is not None:
            return instance

        module = import_module(self.module)
        software_type = getattr(module, self.class_name)
        if not isinstance(software_type, type) or not issubclass(software_type, BaseSoftware):
            raise TypeError(f'{self.module}.{self.class_name} is not a BaseSoftware subclass')

        instance = cast(BaseSoftware, software_type())
        _software_instances[identity] = instance
        return instance


def clear_instantiated_url_cache():
    for software in _software_instances.values():
        software.cached_url = None


def instantiated_software_count() -> int:
    return len(_software_instances)
