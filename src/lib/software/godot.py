from src.lib.software.variants.godot_cs import GodotCS
from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.software.variants.godot_stable import GodotStable

class Godot(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'godot'
        self.name = 'Godot'
        self.category = [SoftwareCategory.Creative, SoftwareCategory.GameDevelopment]
        self.variants = [GodotStable(), GodotCS()]
        self.icon = 'godot.png'
        self.homepage = 'https://godotengine.org'

    def resolve_download_url(self):
        pass
