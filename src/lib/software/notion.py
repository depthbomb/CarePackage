from src.lib.software import BaseSoftware, SoftwareCategory

class Notion(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'notion'
        self.name = 'Notion'
        self.category = [SoftwareCategory.Productivity]
        self.download_name = 'Notion Setup.exe'
        self.icon = 'notion.png'
        self.homepage = 'https://notion.com/desktop'

    def resolve_download_url(self):
        self.url_resolved.emit('https://www.notion.com/desktop/windows/download')
