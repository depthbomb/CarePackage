from src.lib.software import BaseSoftware

class Python312(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'python-312'
        self.name = 'Python 3.12.x'
        self.download_name = 'python3.12.x-amd64.exe'
        self.should_cache_url = True
        self.icon = 'python.png'
        self.homepage = 'https://python.org'

        # Releases after 3.12.10 are source code only
        self._version = '3.12.10'

    def resolve_download_url(self):
        self.url_resolved.emit(f'https://www.python.org/ftp/python/{self._version}/python-{self._version}-amd64.exe')
