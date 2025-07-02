from src.lib.software import BaseSoftware, SoftwareCategory

class Evernote(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'evernote'
        self.name = 'Evernote'
        self.category = [SoftwareCategory.Productivity]
        self.download_name = 'Evernote-latest.exe'
        self.icon = 'evernote.png'
        self.homepage = 'https://evernote.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://win.desktop.evernote.com/builds/Evernote-latest.exe')
