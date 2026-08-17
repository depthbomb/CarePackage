from src.lib.software import BaseSoftware

class Insomnia(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'Insomnia.Core.exe'
        self.silent_install_args = ['--silent']

    def resolve_download_url(self):
        self.url_resolved.emit('https://updates.insomnia.rest/downloads/windows/latest?app=com.insomnia.app&source=website')
