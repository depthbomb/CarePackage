import src.rc.icons  # noqa
import src.rc.images  # noqa
from pathlib import Path
from ctypes import windll
from collections import defaultdict
from PySide6.QtCore import QStandardPaths
from src.lib.software import BaseSoftware
from typing import cast, Type, DefaultDict

_g = globals()

#region Flags
IS_ADMIN = windll.shell32.IsUserAnAdmin() != 0
IS_COMPILED = '__compiled__' in _g
if IS_COMPILED:
    IS_STANDALONE = bool(_g['__compiled__'].standalone)
    IS_ONEFILE = bool(_g['__compiled__'].onefile)
else:
    IS_STANDALONE = False
    IS_ONEFILE = False
#endregion

#region Application Info
APP_NAME = 'carepackage'
APP_DISPLAY_NAME = 'CarePackage'
APP_ORG = 'Caprine Logic'
APP_USER_MODEL_ID = u'CaprineLogic.CarePackage'
APP_VERSION = (2, 3, 5, 0)
APP_VERSION_STRING = '.'.join(str(v) for v in APP_VERSION)
if IS_COMPILED:
    APP_REPO_URL = 'https://bit.ly/carepackage-repo'
    APP_LATEST_RELEASE_URL ='https://bit.ly/get-carepackage'
else:
    APP_REPO_URL = 'https://github.com/depthbomb/CarePackage'
    APP_LATEST_RELEASE_URL = 'https://github.com/depthbomb/CarePackage/releases/latest'
#endregion

#region Strings
USER_AGENT = f'CarePackage/{APP_VERSION_STRING} (depthbomb/carepackage)'
BROWSER_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
#endregion

#region Paths
if IS_COMPILED:
    BINARY_PATH = Path(_g['__compiled__'].original_argv0)
    BINARY_DIR = BINARY_PATH.parent.absolute()
else:
    BINARY_PATH = Path(__file__).parent.parent.absolute()
    # When running directly through Python, there is no 'binary' that the application runs from, so just use the
    # project root directory.
    BINARY_DIR = BINARY_PATH
DOWNLOAD_DIR = Path(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.TempLocation)) / '.carepackage'
APPDATA_DIR = Path(QStandardPaths.writableLocation(QStandardPaths.StandardLocation.AppLocalDataLocation))
DATA_DIR = APPDATA_DIR / APP_ORG / APP_NAME
APP_SETTINGS_FILE_PATH = DATA_DIR / 'app.settings'
USER_SETTINGS_FILE_PATH = DATA_DIR / 'user.settings'
#endregion

#region Software Definitions
from src.lib.software.adobe_creative_cloud import AdobeCreativeCloud
from src.lib.software.apache_netbeans import ApacheNetBeans
from src.lib.software.arc import Arc
from src.lib.software.audacity import Audacity
from src.lib.software.autohotkey import AutoHotkey
from src.lib.software.balenaetcher import BalenaEtcher
from src.lib.software.battlenet import BattleNet
from src.lib.software.bitwarden import Bitwarden
from src.lib.software.blender import Blender
# from src.lib.software.borderless_gaming import BorderlessGaming
from src.lib.software.brave import Brave
from src.lib.software.caesium_image_compressor import CaesiumImageCompressor
from src.lib.software.cmake import CMake
from src.lib.software.corsair_icue import CorsairIcue
from src.lib.software.cpuz import CPUZ
from src.lib.software.db_browser_for_sqlite import DBBrowserForSQLite
from src.lib.software.defraggler import Defraggler
from src.lib.software.discord import Discord
from src.lib.software.display_driver_uninstaller import DisplayDriverUninstaller
from src.lib.software.dnspy import DnSpy
from src.lib.software.docker_desktop import DockerDesktop
from src.lib.software.dolphin_emulator import DolphinEmulator
#region .NET
from src.lib.software.dotnet_6_aspnetcore_runtime import DotNet6AspNetCoreRuntime
from src.lib.software.dotnet_6_desktop_runtime import DotNet6DesktopRuntime
from src.lib.software.dotnet_6_runtime import DotNet6Runtime
from src.lib.software.dotnet_6_sdk import DotNet6Sdk
from src.lib.software.dotnet_8_aspnetcore_runtime import DotNet8AspNetCoreRuntime
from src.lib.software.dotnet_8_desktop_runtime import DotNet8DesktopRuntime
from src.lib.software.dotnet_8_runtime import DotNet8Runtime
from src.lib.software.dotnet_8_sdk import DotNet8Sdk
from src.lib.software.dotnet_9_aspnetcore_runtime import DotNet9AspNetCoreRuntime
from src.lib.software.dotnet_9_desktop_runtime import DotNet9DesktopRuntime
from src.lib.software.dotnet_9_runtime import DotNet9Runtime
from src.lib.software.dotnet_9_sdk import DotNet9Sdk
#endregion
from src.lib.software.dropbox import Dropbox
from src.lib.software.ea_app import EaApp
from src.lib.software.eclipse_ide import EclipseIDE
from src.lib.software.elgato_stream_deck import ElgatoStreamDeck
from src.lib.software.epic_games_launcher import EpicGamesLauncher
from src.lib.software.filezilla import FileZilla
from src.lib.software.flutter_sdk import FlutterSDK
from src.lib.software.foobar2000 import Foobar2000
from src.lib.software.gimp import Gimp
from src.lib.software.git_for_windows import GitForWindows
from src.lib.software.github_cli import GitHubCli
from src.lib.software.github_desktop import GitHubDesktop
from src.lib.software.godot import Godot
from src.lib.software.godot_cs import GodotCS
from src.lib.software.gog_galaxy import GogGalaxy
from src.lib.software.golang import Golang
from src.lib.software.google_chrome import GoogleChrome
from src.lib.software.google_drive import GoogleDrive
from src.lib.software.handbrake import HandBrake
from src.lib.software.heroic_games_launcher import HeroicGamesLauncher
from src.lib.software.hoppscotch import Hoppscotch
from src.lib.software.hwmonitor import HWMonitor
from src.lib.software.inkscape import Inkscape
from src.lib.software.inno_setup import InnoSetup
from src.lib.software.insomnia import Insomnia
from src.lib.software.installforge import InstallForge
from src.lib.software.itunes import ITunes
from src.lib.software.java_sdk_21 import JavaSEDevelopmentKit21
from src.lib.software.java_sdk_23 import JavaSEDevelopmentKit23
from src.lib.software.jetbrains_toolbox import JetBrainsToolbox
from src.lib.software.keepass import KeePass
from src.lib.software.krita import Krita
from src.lib.software.lazarus import Lazarus
from src.lib.software.librewolf import LibreWolf
from src.lib.software.logictech_ghub import LogitechGHub
from src.lib.software.malwarebytes import Malwarebytes
from src.lib.software.medal import Medal
from src.lib.software.microsoft_edge import MicrosoftEdge
from src.lib.software.microsoft_powertoys import MicrosoftPowerToys
from src.lib.software.microsoft_teams import MicrosoftTeams
from src.lib.software.minecraft_launcher import MinecraftLauncher
from src.lib.software.minecraft_launcher_legacy import MinecraftLauncherLegacy
from src.lib.software.mingw import MinGW
from src.lib.software.mozilla_firefox import MozillaFirefox
from src.lib.software.msvc import Msvc
from src.lib.software.msys2 import MSYS2
from src.lib.software.nodejs import NodeJs
from src.lib.software.nodejs_lts import NodeJsLts
from src.lib.software.notepad_plus_plus import NotepadPlusPlus
from src.lib.software.nsis import NSIS
from src.lib.software.nvidia_app import NvidiaApp
from src.lib.software.obs_studio import ObsStudio
from src.lib.software.obsidian import Obsidian
from src.lib.software.onedrive import OneDrive
from src.lib.software.opera import Opera
from src.lib.software.opera_gx import OperaGx
from src.lib.software.oracle_virtualbox import OracleVirtualBox
from src.lib.software.overwolf import Overwolf
from src.lib.software.paintdotnet import PaintDotNet
from src.lib.software.parsec import Parsec
from src.lib.software.pcsx2 import PCSX2
from src.lib.software.playnite import Playnite
from src.lib.software.playstation_accessories import PlayStationAccessories
from src.lib.software.plex_desktop import PlexDesktop
from src.lib.software.plex_media_server import PlexMediaServer
from src.lib.software.plexamp import Plexamp
from src.lib.software.postman import Postman
from src.lib.software.powershell_core import PowerShellCore
from src.lib.software.putty import Putty
from src.lib.software.python_312 import Python312
from src.lib.software.python_313 import Python313
from src.lib.software.qbittorrent import QBitTorrent
from src.lib.software.qt_oss import QtOss
from src.lib.software.raspberry_pi_imager import RaspberryPiImager
from src.lib.software.razer_cortex import RazerCortex
from src.lib.software.revolt import Revolt
from src.lib.software.rufus import Rufus
from src.lib.software.rustup import Rustup
from src.lib.software.sevenzip import SevenZip
from src.lib.software.sharex import ShareX
from src.lib.software.signal import Signal
from src.lib.software.skype import Skype
from src.lib.software.slack import Slack
from src.lib.software.speccy import Speccy
from src.lib.software.spotify import Spotify
from src.lib.software.steam import Steam
from src.lib.software.streamlabs_desktop import StreamlabsDesktop
from src.lib.software.streamlink import Streamlink
from src.lib.software.sublime_text import SublimeText
from src.lib.software.system_informer import SystemInformer
from src.lib.software.teamviewer import TeamViewer
from src.lib.software.telegram_desktop import TelegramDesktop
from src.lib.software.teracopy import TeraCopy
from src.lib.software.thunderbird import Thunderbird
from src.lib.software.ubisoft_connect import UbisoftConnect
from src.lib.software.unity_hub import UnityHub
from src.lib.software.visual_studio_code import VisualStudioCode
from src.lib.software.visual_studio_community import VisualStudioCommunity
from src.lib.software.vivaldi import Vivaldi
from src.lib.software.vlc_media_player import VlcMediaPlayer
from src.lib.software.waterfox import Waterfox
from src.lib.software.webview2_runtime import WebView2Runtime
from src.lib.software.windirstat import WinDirStat
from src.lib.software.winrar import Winrar
from src.lib.software.winscp import WinScp
from src.lib.software.zulip import Zulip

ALL_SOFTWARE = cast(list[Type[BaseSoftware]], [
    AdobeCreativeCloud,
    ApacheNetBeans,
    Arc,
    Audacity,
    AutoHotkey,
    BalenaEtcher,
    BattleNet,
    Bitwarden,
    Blender,
    # BorderlessGaming,
    Brave,
    CaesiumImageCompressor,
    CMake,
    CorsairIcue,
    CPUZ,
    DBBrowserForSQLite,
    Defraggler,
    Discord,
    DisplayDriverUninstaller,
    DnSpy,
    DockerDesktop,
    DolphinEmulator,
    DotNet6AspNetCoreRuntime,
    DotNet6DesktopRuntime,
    DotNet6Runtime,
    DotNet6Sdk,
    DotNet8AspNetCoreRuntime,
    DotNet8DesktopRuntime,
    DotNet8Runtime,
    DotNet8Sdk,
    DotNet9AspNetCoreRuntime,
    DotNet9DesktopRuntime,
    DotNet9Runtime,
    DotNet9Sdk,
    Dropbox,
    EaApp,
    EclipseIDE,
    ElgatoStreamDeck,
    EpicGamesLauncher,
    FileZilla,
    FlutterSDK,
    Foobar2000,
    Gimp,
    GitForWindows,
    GitHubCli,
    GitHubDesktop,
    Godot,
    GodotCS,
    GogGalaxy,
    Golang,
    GoogleChrome,
    GoogleDrive,
    HandBrake,
    HeroicGamesLauncher,
    Hoppscotch,
    HWMonitor,
    Inkscape,
    InnoSetup,
    Insomnia,
    InstallForge,
    ITunes,
    JavaSEDevelopmentKit21,
    JavaSEDevelopmentKit23,
    JetBrainsToolbox,
    KeePass,
    Krita,
    Lazarus,
    LibreWolf,
    LogitechGHub,
    Malwarebytes,
    Medal,
    MicrosoftEdge,
    MicrosoftPowerToys,
    MicrosoftTeams,
    MinecraftLauncher,
    MinecraftLauncherLegacy,
    MinGW,
    MozillaFirefox,
    Msvc,
    MSYS2,
    NodeJs,
    NodeJsLts,
    NotepadPlusPlus,
    NSIS,
    NvidiaApp,
    ObsStudio,
    Obsidian,
    OneDrive,
    Opera,
    OperaGx,
    OracleVirtualBox,
    Overwolf,
    PaintDotNet,
    Parsec,
    PCSX2,
    Playnite,
    PlayStationAccessories,
    PlexDesktop,
    PlexMediaServer,
    Plexamp,
    Postman,
    PowerShellCore,
    Putty,
    Python312,
    Python313,
    QBitTorrent,
    QtOss,
    RaspberryPiImager,
    RazerCortex,
    Revolt,
    Rufus,
    Rustup,
    SevenZip,
    ShareX,
    Signal,
    Skype,
    Slack,
    Speccy,
    Spotify,
    Steam,
    StreamlabsDesktop,
    Streamlink,
    SublimeText,
    SystemInformer,
    TeamViewer,
    TelegramDesktop,
    TeraCopy,
    Thunderbird,
    UbisoftConnect,
    UnityHub,
    VisualStudioCode,
    VisualStudioCommunity,
    Vivaldi,
    VlcMediaPlayer,
    Waterfox,
    WebView2Runtime,
    WinDirStat,
    Winrar,
    WinScp,
    Zulip,
])
SOFTWARE_CATALOGUE = cast(DefaultDict[str, list[BaseSoftware]], defaultdict(list))
for software in ALL_SOFTWARE:
    instance = software()
    SOFTWARE_CATALOGUE[instance.category].append(instance)
#endregion
