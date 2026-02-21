import src.rc.fonts  # noqa
import src.rc.icons  # noqa
import src.rc.images  # noqa
from pathlib import Path
from typing import cast, Type
from PySide6.QtCore import QStandardPaths
from src.lib.software import BaseSoftware

_g = globals()

#region Flags
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
APP_DESCRIPTION = 'Software Management Tool'
APP_ORG = 'Caprine Logic'
APP_USER_MODEL_ID = u'CaprineLogic.CarePackage'
APP_CLSID = 'C3B0021E-33B6-4ECC-97D2-E6A3CAF6A11B'
APP_VERSION = (4, 3, 8, 0)
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
BROWSER_USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'
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

#region Software Definitions
from src.lib.software.abdownloadmanager import ABDownloadManager
from src.lib.software.adobe_creative_cloud import AdobeCreativeCloud
from src.lib.software.aimp import Aimp
from src.lib.software.apache_netbeans import ApacheNetBeans
from src.lib.software.audacity import Audacity
from src.lib.software.autohotkey import AutoHotkey
from src.lib.software.azahar import Azahar
from src.lib.software.balenaetcher import BalenaEtcher
from src.lib.software.battlenet import BattleNet
from src.lib.software.bitwarden import Bitwarden
from src.lib.software.blender import Blender
from src.lib.software.brave import Brave
from src.lib.software.caesium_image_compressor import CaesiumImageCompressor
from src.lib.software.calibre import Calibre
from src.lib.software.ccleaner import Ccleaner
from src.lib.software.cemu import Cemu
from src.lib.software.cheat_engine import CheatEngine
from src.lib.software.clink import Clink
from src.lib.software.cmake import CMake
from src.lib.software.composer import Composer
from src.lib.software.corsair_icue import CorsairIcue
from src.lib.software.cpuz import CPUZ
from src.lib.software.darktable import Darktable
from src.lib.software.db_browser_for_sqlite import DBBrowserForSQLite
from src.lib.software.defraggler import Defraggler
from src.lib.software.discord import Discord
from src.lib.software.display_driver_uninstaller import DisplayDriverUninstaller
from src.lib.software.dnspy import DnSpy
from src.lib.software.docker_desktop import DockerDesktop
from src.lib.software.dolphin_emulator import DolphinEmulator
from src.lib.software.dotnet import DotNet
from src.lib.software.dropbox import Dropbox
from src.lib.software.duckstation import DuckStation
from src.lib.software.ea_app import EaApp
from src.lib.software.eclipse_ide import EclipseIDE
from src.lib.software.elgato_stream_deck import ElgatoStreamDeck
from src.lib.software.epic_games_launcher import EpicGamesLauncher
from src.lib.software.equalizer_apo import EqualizerApo
from src.lib.software.evernote import Evernote
from src.lib.software.everything import Everything
from src.lib.software.flutter_sdk import FlutterSDK
from src.lib.software.foobar2000 import Foobar2000
from src.lib.software.gimp import Gimp
from src.lib.software.git_for_windows import GitForWindows
from src.lib.software.github_cli import GitHubCli
from src.lib.software.github_desktop import GitHubDesktop
from src.lib.software.glasswire import GlassWire
from src.lib.software.godot import Godot
from src.lib.software.gog_galaxy import GogGalaxy
from src.lib.software.golang import Golang
from src.lib.software.google_chrome import GoogleChrome
from src.lib.software.google_drive import GoogleDrive
from src.lib.software.gpg4win import Gpg4win
from src.lib.software.handbrake import HandBrake
from src.lib.software.heroic_games_launcher import HeroicGamesLauncher
from src.lib.software.hoppscotch import Hoppscotch
from src.lib.software.hwmonitor import HWMonitor
from src.lib.software.icloud_for_windows import ICloudForWindows
from src.lib.software.inkscape import Inkscape
from src.lib.software.inno_setup import InnoSetup
from src.lib.software.insomnia import Insomnia
from src.lib.software.installforge import InstallForge
from src.lib.software.itch import Itch
from src.lib.software.itunes import ITunes
from src.lib.software.jackett import Jackett
from src.lib.software.java_sdk import JavaSEDevelopmentKit
from src.lib.software.jetbrains_toolbox import JetBrainsToolbox
from src.lib.software.joplin import Joplin
from src.lib.software.keepassxc import KeePassXC
from src.lib.software.krita import Krita
from src.lib.software.lazarus import Lazarus
from src.lib.software.libreoffice import LibreOffice
from src.lib.software.librewolf import LibreWolf
from src.lib.software.lightshot import Lightshot
from src.lib.software.logictech_ghub import LogitechGHub
from src.lib.software.malwarebytes import Malwarebytes
from src.lib.software.medal import Medal
from src.lib.software.megasync import Megasync
from src.lib.software.melonds import MelonDs
from src.lib.software.mgba import MGBA
from src.lib.software.microsoft_edge import MicrosoftEdge
from src.lib.software.microsoft_powertoys import MicrosoftPowerToys
from src.lib.software.microsoft_teams import MicrosoftTeams
from src.lib.software.minecraft import Minecraft
from src.lib.software.mingw import MinGW
from src.lib.software.moonlight import Moonlight
from src.lib.software.motrix import Motrix
from src.lib.software.mozilla_firefox import MozillaFirefox
from src.lib.software.mpv import MPV
from src.lib.software.msi_afterburner import MSIAfterburner
from src.lib.software.msvc import Msvc
from src.lib.software.msys2 import MSYS2
from src.lib.software.mullvad_vpn import MullvadVPN
from src.lib.software.nodejs import NodeJs
from src.lib.software.notepad_plus_plus import NotepadPlusPlus
from src.lib.software.notion import Notion
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
from src.lib.software.peazip import PeaZip
from src.lib.software.pgadmin4 import PgAdmin4
from src.lib.software.php import PHP
from src.lib.software.playnite import Playnite
from src.lib.software.playstation_accessories import PlayStationAccessories
from src.lib.software.plex import Plex
from src.lib.software.postman import Postman
from src.lib.software.powershell_core import PowerShellCore
from src.lib.software.ppsspp import Ppsspp
from src.lib.software.putty import Putty
from src.lib.software.pymanager import PyManager
from src.lib.software.python import Python
from src.lib.software.qbittorrent import QBitTorrent
from src.lib.software.qt_oss import QtOss
from src.lib.software.rainmeter import Rainmeter
from src.lib.software.raspberry_pi_imager import RaspberryPiImager
from src.lib.software.razer_cortex import RazerCortex
from src.lib.software.recuva import Recuva
from src.lib.software.revolt import Revolt
from src.lib.software.rockstar_games_launcher import RockstarGamesLauncher
from src.lib.software.rpcs3 import RPCS3
from src.lib.software.rufus import Rufus
from src.lib.software.rustup import Rustup
from src.lib.software.sevenzip import SevenZip
from src.lib.software.shadps4 import ShadPS4
from src.lib.software.sharex import ShareX
from src.lib.software.shotcut import Shotcut
from src.lib.software.signal import Signal
from src.lib.software.slack import Slack
from src.lib.software.snes9x import Snes9X
from src.lib.software.speccy import Speccy
from src.lib.software.spotify import Spotify
from src.lib.software.steam import Steam
from src.lib.software.streamlabs_desktop import StreamlabsDesktop
from src.lib.software.streamlink import Streamlink
from src.lib.software.sublime_text import SublimeText
from src.lib.software.sumatrapdf import SumatraPDF
from src.lib.software.sunshine import Sunshine
from src.lib.software.system_informer import SystemInformer
from src.lib.software.teamviewer import TeamViewer
from src.lib.software.telegram_desktop import TelegramDesktop
from src.lib.software.temurin import TemurinJDK
from src.lib.software.teracopy import TeraCopy
from src.lib.software.thunderbird import Thunderbird
from src.lib.software.tor_browser import TorBrowser
from src.lib.software.treesize_free import TreeSizeFree
from src.lib.software.trillian import Trillian
from src.lib.software.ubisoft_connect import UbisoftConnect
from src.lib.software.unity_hub import UnityHub
from src.lib.software.veracrypt import VeraCrypt
from src.lib.software.visual_studio_code import VisualStudioCode
from src.lib.software.visual_studio_community import VisualStudioCommunity
from src.lib.software.vita3k import Vita3k
from src.lib.software.vivaldi import Vivaldi
from src.lib.software.vlc_media_player import VlcMediaPlayer
from src.lib.software.waterfox import Waterfox
from src.lib.software.webview2_runtime import WebView2Runtime
from src.lib.software.wemod import WeMod
from src.lib.software.whatsapp import WhatsApp
from src.lib.software.windirstat import WinDirStat
from src.lib.software.windows_app_sdk import WindowsAppSdk
from src.lib.software.winrar import Winrar
from src.lib.software.winscp import WinScp
from src.lib.software.wireshark import Wireshark
from src.lib.software.yay import Yay
from src.lib.software.zoom import Zoom
from src.lib.software.zulip import Zulip

ALL_SOFTWARE = cast(list[Type[BaseSoftware]], [
    ABDownloadManager,
    AdobeCreativeCloud,
    Aimp,
    ApacheNetBeans,
    Audacity,
    AutoHotkey,
    Azahar,
    BalenaEtcher,
    BattleNet,
    Bitwarden,
    Blender,
    Brave,
    CaesiumImageCompressor,
    Calibre,
    Ccleaner,
    Cemu,
    CheatEngine,
    Clink,
    CMake,
    Composer,
    CorsairIcue,
    CPUZ,
    Darktable,
    DBBrowserForSQLite,
    Defraggler,
    Discord,
    DisplayDriverUninstaller,
    DnSpy,
    DockerDesktop,
    DolphinEmulator,
    DotNet,
    Dropbox,
    DuckStation,
    EaApp,
    EclipseIDE,
    ElgatoStreamDeck,
    EpicGamesLauncher,
    EqualizerApo,
    Evernote,
    Everything,
    FlutterSDK,
    Foobar2000,
    Gimp,
    GitForWindows,
    GitHubCli,
    GitHubDesktop,
    GlassWire,
    Godot,
    GogGalaxy,
    Golang,
    GoogleChrome,
    GoogleDrive,
    Gpg4win,
    HandBrake,
    HeroicGamesLauncher,
    Hoppscotch,
    HWMonitor,
    ICloudForWindows,
    Inkscape,
    InnoSetup,
    Insomnia,
    InstallForge,
    Itch,
    ITunes,
    Jackett,
    JavaSEDevelopmentKit,
    JetBrainsToolbox,
    Joplin,
    KeePassXC,
    Krita,
    Lazarus,
    LibreOffice,
    LibreWolf,
    Lightshot,
    LogitechGHub,
    Malwarebytes,
    Medal,
    Megasync,
    MelonDs,
    MGBA,
    MicrosoftEdge,
    MicrosoftPowerToys,
    MicrosoftTeams,
    Minecraft,
    MinGW,
    Moonlight,
    Motrix,
    MozillaFirefox,
    MPV,
    MSIAfterburner,
    Msvc,
    MSYS2,
    MullvadVPN,
    NodeJs,
    NotepadPlusPlus,
    Notion,
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
    PeaZip,
    PgAdmin4,
    PHP,
    Playnite,
    PlayStationAccessories,
    Plex,
    Postman,
    PowerShellCore,
    Ppsspp,
    Putty,
    PyManager,
    Python,
    QBitTorrent,
    QtOss,
    Rainmeter,
    RaspberryPiImager,
    RazerCortex,
    Recuva,
    Revolt,
    RockstarGamesLauncher,
    RPCS3,
    Rufus,
    Rustup,
    SevenZip,
    ShadPS4,
    ShareX,
    Shotcut,
    Signal,
    Slack,
    Snes9X,
    Speccy,
    Spotify,
    Steam,
    StreamlabsDesktop,
    Streamlink,
    SublimeText,
    SumatraPDF,
    Sunshine,
    SystemInformer,
    TeamViewer,
    TelegramDesktop,
    TemurinJDK,
    TeraCopy,
    Thunderbird,
    TorBrowser,
    TreeSizeFree,
    Trillian,
    UbisoftConnect,
    UnityHub,
    VeraCrypt,
    VisualStudioCode,
    VisualStudioCommunity,
    Vita3k,
    Vivaldi,
    VlcMediaPlayer,
    Waterfox,
    WebView2Runtime,
    WeMod,
    WhatsApp,
    WinDirStat,
    Winrar,
    WinScp,
    WindowsAppSdk,
    Wireshark,
    Yay,
    Zoom,
    Zulip,
])
SOFTWARE_CATALOGUE = cast(list[BaseSoftware], [])
for software in ALL_SOFTWARE:
    instance = software()
    SOFTWARE_CATALOGUE.append(instance)
#endregion
