from src.lib.software import BaseSoftware, SoftwareCategory

class DotNet6Runtime(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'dotnet-6-runtime'
        self.name = '.NET 6.0 Runtime'
        self.category = SoftwareCategory.DotNet
        self.download_name = 'dotnet-runtime-6.0-win-x64.exe'
        self.is_archive = False
        self.should_cache_url = False
        self.requires_admin = False
        self.icon = 'dotnet.png'
        self.homepage = 'https://dot.net'

    def resolve_download_url(self):
        self.url_resolved.emit('https://download.visualstudio.microsoft.com/download/pr/1a5fc50a-9222-4f33-8f73-3c78485a55c7/1cb55899b68fcb9d98d206ba56f28b66/dotnet-runtime-6.0.36-win-x64.exe')
