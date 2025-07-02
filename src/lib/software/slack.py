from src.lib.software import BaseSoftware, SoftwareCategory

class Slack(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'slack'
        self.name = 'Slack'
        self.category = [SoftwareCategory.Social]
        self.download_name = 'SlackSetup.exe'
        self.icon = 'slack.png'
        self.homepage = 'https://slack.com'

    def resolve_download_url(self):
        self.url_resolved.emit('https://slack.com/api/desktop.latestRelease?arch=x64&variant=exe&redirect=true')
