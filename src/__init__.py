import src.rc.fonts  # noqa
import src.rc.icons  # noqa
import src.rc.images  # noqa
from pathlib import Path
from platform import system, version
from PySide6.QtCore import QStandardPaths
from src.software_catalogue import SOFTWARE_CATALOGUE

_g = globals()

#region Flags
IS_COMPILED = '__compiled__' in _g
if IS_COMPILED:
    IS_STANDALONE = bool(_g['__compiled__'].standalone)
    IS_ONEFILE = bool(_g['__compiled__'].onefile)
else:
    IS_STANDALONE = False
    IS_ONEFILE = False

IS_WINDOWS11 = system() == 'Windows' and int(version().split('.')[-1]) >= 22_000

#endregion

#region Application Info
APP_NAME = 'carepackage'
APP_DISPLAY_NAME = 'CarePackage'
APP_DESCRIPTION = 'Software Management Tool'
APP_ORG = 'Caprine Logic'
APP_USER_MODEL_ID = u'CaprineLogic.CarePackage'
APP_CLSID = 'C3B0021E-33B6-4ECC-97D2-E6A3CAF6A11B'
APP_VERSION = (5, 0, 1, 0)
APP_VERSION_STRING = '.'.join(str(v) for v in APP_VERSION)
APP_REPO_OWNER = 'depthbomb'
APP_REPO_NAME = 'CarePackage'
APP_REPO_URL = f'https://github.com/{APP_REPO_OWNER}/{APP_REPO_NAME}'
APP_RELEASES_URL = f'https://github.com/{APP_REPO_OWNER}/{APP_REPO_NAME}/releases'
APP_LATEST_RELEASE_URL = f'https://github.com/{APP_REPO_OWNER}/{APP_REPO_NAME}/releases/latest'
APP_NEW_ISSUE_URL = f'https://github.com/{APP_REPO_OWNER}/{APP_REPO_NAME}/issues/new/choose'
#endregion

#region Strings
USER_AGENT = f'{APP_DISPLAY_NAME}/{APP_VERSION_STRING} ({APP_REPO_OWNER}/{APP_REPO_NAME})'
BROWSER_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/151.0.0.0 Safari/537.36'
#endregion

#region Paths
if IS_COMPILED:
    BINARY_PATH = Path(_g['__compiled__'].original_argv0)
    BINARY_DIR = BINARY_PATH.parent.absolute()
else:
    BINARY_PATH = Path(__file__).parent.parent.absolute()
    # When running directly through Python there is no 'binary' that the application runs from so just use the project
    # root directory.
    BINARY_DIR = BINARY_PATH
DOWNLOAD_DIR = Path(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.TempLocation)) / '.carepackage'
APPDATA_DIR = Path(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppDataLocation))
DATA_DIR = APPDATA_DIR / APP_ORG / APP_NAME
SETTINGS_FILE_PATH = DATA_DIR / 'client_prefs.bin'
#endregion
