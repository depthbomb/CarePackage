from src.lib.software import BaseSoftware, SoftwareCategory
from src.lib.software.variants.dotnet_8_sdk import DotNet8Sdk
from src.lib.software.variants.dotnet_9_sdk import DotNet9Sdk
from src.lib.software.variants.dotnet_8_runtime import DotNet8Runtime
from src.lib.software.variants.dotnet_9_runtime import DotNet9Runtime
from src.lib.software.variants.dotnet_8_desktop_runtime import DotNet8DesktopRuntime
from src.lib.software.variants.dotnet_9_desktop_runtime import DotNet9DesktopRuntime
from src.lib.software.variants.dotnet_8_aspnetcore_runtime import DotNet8AspNetCoreRuntime
from src.lib.software.variants.dotnet_9_aspnetcore_runtime import DotNet9AspNetCoreRuntime

class DotNet(BaseSoftware):
    def __init__(self):
        super().__init__()

        self.key = 'dotnet'
        self.name = '.NET'
        self.category = [SoftwareCategory.Development, SoftwareCategory.Runtime]
        self.variants = [
            DotNet8AspNetCoreRuntime(),
            DotNet8DesktopRuntime(),
            DotNet8Runtime(),
            DotNet8Sdk(),
            DotNet9AspNetCoreRuntime(),
            DotNet9DesktopRuntime(),
            DotNet9Runtime(),
            DotNet9Sdk(),
        ]
        self.icon = 'dotnet.png'
        self.homepage = 'https://dot.net'

    def resolve_download_url(self):
        pass
