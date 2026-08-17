from src.lib.software import BaseSoftware

class Evernote(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'Evernote-latest.exe'
        self.silent_install_args = ['/S']

    def resolve_download_url(self):
        self.url_resolved.emit('https://win.desktop.evernote.com/builds/Evernote-latest.exe')
