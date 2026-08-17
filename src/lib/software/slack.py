from src.lib.software import BaseSoftware

class Slack(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.download_name = 'SlackSetup.exe'
        self.silent_install_args = ['--silent']

    def resolve_download_url(self):
        self.url_resolved.emit('https://slack.com/api/desktop.latestRelease?arch=x64&variant=exe&redirect=true')
