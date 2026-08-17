from src.lib.software import BaseSoftware

class Rustup(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'rustup-init.exe'

    def resolve_download_url(self):
        self.url_resolved.emit('https://static.rust-lang.org/rustup/dist/x86_64-pc-windows-msvc/rustup-init.exe')
