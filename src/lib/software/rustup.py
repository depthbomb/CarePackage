from src.lib.software import BaseSoftware, SoftwareCategory

class Rustup(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'rustup'
        self.name = 'Rustup'
        self.category = SoftwareCategory.Development
        self.download_name = 'rustup-init.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'rust.png'
        self.homepage = 'https://www.rust-lang.org/learn/get-started'

    def resolve_download_url(self):
        self.url_resolved.emit('https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe')
