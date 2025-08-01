﻿# 4.3.2

- Fixed a potential crash when running the application for the very first time
- The total size of downloaded files is displayed before and after sweeping
- Fixed download URL resolving for _OBS Studio_
- Added software: _WeMod_

# 4.3.1

- Only one instance of _CarePackage_ can be running at once, subsequent instances will close and the original instance will be focused
- Adjusted the style of software rows when using various app style and theme combinations
- Fixed the "System" app theme defaulting to the light theme
- The software variant wizard window will now use the dark titlebar color if the system is using dark mode
- Adjusted the style of the software variant window

# 4.3.0

- Added an option to change the application's theme
- Fixed the extended titlebar button icons not using the correct theme based on the system's accent color
- Fixed badge text not using the correct foreground color based on the system's accent color
- Due to an overhaul of the underlying settings system, your configuration has been reset
  - The settings file is now written in a binary format
  - The app's data directory is now located at `%APPDATA%\Caprine Logic\carepackage` instead of `%LOCALAPPDATA%\Caprine Logic\carepackage`
- Added the following software:
  - _calibre_
  - _Mullvad VPN_
  - _SumatraPDF_
- Fixed download URL resolving for the following software:
  - _PHP (Thread Safe)_
- Known issues:
  - Download URL resolving for _FileZilla_ may fail

# 4.2.3

- Adjusted the shades of accent colors in some places
- Icons will now be black if the accent color is too bright
- Adjusted the style of category badges
- Fixed a debug option appearing in the settings window
- Upgraded to Python 3.13

# 4.2.2

- A dialog box is now shown that lets you open CarePackage's latest release page if an update is available on app startup
- Added the following software:
  - _Moonlight_
  - _Sunshine_

# 4.2.1

- Updated the "Writing to disk" status message for large file downloads
- Added the following software:
  - _Composer_
  - _Gpg4win_
  - _pgAdmin 4_
  - _PHP_
  - _Rockstar Games Launcher_

# 4.2.0

- The app now always runs as administrator, getting rid of the warning and requirement to restart the app when trying to install software that requires administrator privileges
- Added the following software:
  - _AB Download Manager_
- Improved download URL resolving for the following software:
  - _.NET 8.0 ASP.NET Core Runtime_
  - _.NET 8.0 Desktop Runtime_
  - _.NET 8.0 Runtime_
  - _.NET 8.0 SDK_
  - _.NET 9.0 ASP.NET Core Runtime_
  - _.NET 9.0 Desktop Runtime_
  - _.NET 9.0 Runtime_
  - _.NET 9.0 SDK_

# 4.1.1

__This release is a hotfix. There are no notable changes.__ The previous release's changelog is below.

- Fixed a crash that would occur when opening the settings window immediately after a fresh install
- The dark window titlebar and border will not be used if the system is not using dark mode
- Adjusted the color of selected software
- The homepage for software variants can now be accessed from the variant picker window
- Variants now show if they require administrator privileges or are an archive in the variant picker window
- Added the following software:
  - _Everything_ (standard, lite, and CLI)
  - _iCloud for Windows_
  - _mpv_
  - _MSI Afterburner_ (final and beta)
  - _Notion_
  - _Tor Browser_
  - _TreeSize Free_
  - _VeraCrypt_
  - _WhatsApp_
  - _yay_

# 4.1.0

- Fixed a crash that would occur when opening the settings window immediately after a fresh install
- The dark window titlebar and border will not be used if the system is not using dark mode
- Adjusted the color of selected software
- The homepage for software variants can now be accessed from the variant picker window
- Variants now show if they require administrator privileges or are an archive in the variant picker window
- Added the following software:
  - _Everything_ (standard, lite, and CLI)
  - _iCloud for Windows_
  - _mpv_
  - _MSI Afterburner_ (final and beta)
  - _Notion_
  - _Tor Browser_
  - _TreeSize Free_
  - _VeraCrypt_
  - _WhatsApp_
  - _yay_

# 4.0.0

This release is not quite a rewrite but rather going back to the pre-3.0.0 version of _CarePackage_ and bringing it up to the standards, in terms of features, of the 3.0.0 version.

This change was made due to various oddities caused by the new backend architecture of 3.0.0 and because there was already a solid foundation in pre-3.0.0. Also, the file size of the application will again be significantly smaller.

The following changes have been ported from 3.0.0:
- Added UWP visual elements
- You can now search for software by text
- Filtering by category is now done via a selection box rather than tabs
- Added hotkeys:
  - `CTRL+A` selects all software currently displayed in the catalogue
  - `CTRL+D` deselects all selected software
- Extra info about software, such as being able to visit their homepage, can now be accessed by right-clicking them
- The number of selected software is now displayed
- Installation options and download queue are now part of the main window
- Selected software is persisted after restarting the app as administrator
- Software can now be in multiple categories
- The categories that each software belongs to are now shown in its row

Additionally, the following changes are brand new:
- Using the search box now searches in the selected category instead of only among all categories
- The search box now has a clear button

Known issues:
- UI icons may be hard to see or the incorrect color depending on the system's accent color
- The app may rarely crash when opening the settings window

# 3.4.0

- Your system's accent color will now be used for styling various UI elements
- The download options screen now shows what software is in the queue
- Settings can now be accessed while an operation is running
- Software icons are now loaded from the app's resource archive instead of directly from the file system
- Updated the app's icon and start menu assets

# 3.3.0

- Software can now have "variants"
  - Variants are used when software has multiple versions that you may want to download and install over another, for example _Discord_ has the variants _Discord Canary_ and _Discord PTB_
  - Clicking a software row that has variants will present you with a selection modal to select its variants
- The following software now have variants:
  - All _.NET_-related software
  - _Discord_
  - _Godot_
  - _Java SDK_
  - _Minecraft Launcher_
  - _Node.js_
  - _Plex_
  - _Python_
- Removed the _.NET_ category

# 3.2.0

- Fixed the settings button being disabled after cancelling an operation
- Fixed download URL failing to resolve for _FileZilla_
- Download-related settings no longer require an app restart to apply
- Downloaded software is removed from the queue when opting to skip installation
- Update link now leads to the original URL rather than going through bit.ly
- Added the new _System Management_ category
- Added _CCleaner_

# 3.1.1

- Fixed restarting as administrator not persisting selected software

# 3.1.0

- Removed keybinds as they caused too many conflicts with other parts of the UI
- Removed _Max connections per download_ option as changing it can cause issues when downloading from some sources
- Improved handling of failed downloads
- Fixed download URL resolving for the following software:
  - _Inno Setup_
  - _Streamlabs Desktop_
- Added the following software:
  - _AIMP_
  - _Evernote_
  - _Jackett_
  - _LibreOffice_
  - _Motrix_
  - _Trillian_
  - _Windows App SDK_

# 3.0.0

This release brings yet another complete rewrite of _CarePackage_ along with the following features:

- New logo
- Added UWP visual elements
- You can now search for software by text
- Filtering by category is now done via a selection box rather than tabs
- ~~Added hotkeys:~~
  - ~~`CTRL+A` selects all software currently displayed in the catalogue~~
  - ~~`CTRL+D` deselects all selected software~~
  - ~~`ENTER` proceeds to the next step~~
  - ~~`ESCAPE` cancels the download and installation process~~
- Extra info about software, such as being able to visit their homepage, can now be accessed by right-clicking them
- The number of selected software is now displayed
- Installation options and download queue are now part of the main window
- Hovering over options on the options screen now shows detailed info about the option
- Restarts and shutdown post-operation actions are now delayed instead of instantly happening
- Selected software is persisted after restarting the app as administrator
- Portable distributions have been discontinued
- Software downloads are now handled with [aria2](https://aria2.github.io)
- Files can now be downloaded concurrently
- Added an option to control how many attempts will be made to download a file
- Added an option to control how many files are downloaded concurrently
- Added an option to control the file download speed
- ~~Added an option to control the maximum connections per for each download~~
- Software can now be in multiple categories
- The categories that each software belongs to is now shown in its row
- Added the following new categories:
  - _3D Modelling_
  - _Audio & Sound_
  - _Emulation_
  - _File Management_
  - _Network Tools_
  - _Notes & Productivity_
- Updated the categories of various software
- Updated icon for _GIMP_
- Improved download URL resolving for the following software:
  - _.NET 8.0 ASP.NET Core Runtime_
  - _.NET 8.0 Desktop Runtime_
  - _.NET 8.0 Runtime_
  - _.NET 8.0 SDK_
  - _.NET 9.0 ASP.NET Core Runtime_
  - _.NET 9.0 Desktop Runtime_
  - _.NET 9.0 Runtime_
  - _.NET 9.0 SDK_
  - _Apache NetBeans_
  - _Blender_
  - _Node.js_
  - _Node.js (LTS)_
  - _NSIS_
  - _Python 3.12.x_
  - _Python 3.13.x_
- Added the following software:
  - _Azahar_
  - _Cemu_
  - _Cheat Engine_
  - _darktable_
  - _DuckStation_
  - _Equalizer APO_
  - _GlassWire_
  - _itch_
  - _Java SE Development Kit 24.x_
  - _Joplin_
  - _LightShot_
  - _MEGAsync_
  - _melonDS_
  - _PeaZip_
  - _PPSSPP_
  - _Rainmeter_
  - _Recuva_
  - _RPCS3_
  - _ShadPS4_
  - _Vita3K_
  - _Wireshark_
  - _Zoom_
- Removed the following software:
  - _.NET 6.0 ASP.NET Core Runtime_
  - _.NET 6.0 Desktop Runtime_
  - _.NET 6.0 Runtime_
  - _.NET 6.0 SDK_
  - _Skype_
  - _Java SE Development Kit 23.x_

# 2.3.5.0

- Fixed failing to resolve download URL for _KeePass_
- Removed _Borderless Gaming_ as they have removed binaries from all releases 🙄

# 2.3.4.0

- Added the following software:
  - Java SE Development Kit 23
  - Java SE Development Kit 21
  - CPU-Z
  - HWMonitor
- Renamed _PowerToys_ to _Microsoft PowerToys (Preview)_

# 2.3.3.0

- Updated to Qt 6.8.2
- Fixed _Display Driver Uninstaller_ failing to download due to download URL changes
- Removed _NVIDIA GeForce Experience_

# 2.3.2.0

- Fixed URL resolving for the following software:
  - _Defraggler_
  - _Speccy_
- Added _GitHub Desktop_

# 2.3.1.0

- When enabled, the download folder will only be opened if at least one selected software downloads successfully
- Fixed _Bitwarden_ being in the incorrect category
- Added the following software:
  - _balenaEtcher_
  - _Raspberry Pi Imager_
  - _Obsidian_
  - _Heroic Games Launcher_
  - _TeraCopy_
  - _Medal_
  - _Hoppscotch_

# 2.3.0.0

- Added _iTunes_
- Software may now be marked as _deprecated_ meaning that it is no longer recommended
  - Deprecated software may be removed from CarePackage in the future
  - Alternatives may be recommended when selecting deprecated software
- Fixed the download URL for _NVIDIA GeForce Experience_ failing to resolve
- _NVIDIA GeForce Experience_ has been marked as deprecated

# 2.2.1.0

- Added the following software:
  - _Adobe Creative Cloud_
  - _NSIS_
  - _InstallForge_
- Moved _Node.js_ and _Node.js (LTS)_ to the _Development_ category
- Fixed software that download from GitHub releases not going into an error state and holding up the queue if a release could not be found
- Fixed _Apache NetBeans_ using the wrong error state when it fails to resolve a URL
- Fixed _Apache NetBeans_ sometimes not being put in an error state when it should and holding up the queue
- Fixed _Python 3.12.x_ using the wrong error state when it fails to resolve a URL
- Fixed _Python 3.12.x_ sometimes not being put in an error state when it should and holding up the queue

# 2.2.0.0

- Renamed the _Creative Tools_ category to _Creative_
- Updated the design of the operation window:
  - Current download speed is now displayed while software is downloading
  - The download progress bar will now replace the software name when possible
  - Changed spinner style
- Update checking is now enabled for portable installations
- The operation window will now scroll to the software that has just started downloading
- Adjusted some software so that they are not flagged as requiring admin privileges
- Fixed some cases where software that errored during the installation step would not show an erroneous status
- Added the following software:
  - _Playnite_
  - _Waterfox_
  - _LibreWolf_
  - _Vivaldi_
  - _AutoHotkey_
  - _Plexamp_
  - _Git for Windows_
  - _Docker Desktop_
  - _Bitwarden_
  - _KeePass_
  - _Razer Cortex_
  - _Signal_
  - _Zulip_
  - _Slack_
  - _Microsoft Teams_
  - _Rufus_
  - _Display Driver Uninstaller_
  - _Eclipse IDE_
  - _CMake_
  - _Oracle VirtualBox_
  - _Apache NetBeans_
  - _Revolt_
  - _Sublime Text_
  - _Godot_
  - _Lazarus_
  - _MinGW_
  - _MSYS2_
  - _Flutter SDK_
  - _Inno Setup_

# 2.1.1.1

- Fixed downloads timing out on portable installations
- Changed the default timeout for downloads to 5 minutes

# 2.1.1.0

- Adjusted size of the software suggestion window
- Adjusted the color of progress bars when using the _Fusion_ theme

# 2.1.0.0

- Added a setting to show the number of software for each category's tab
- Default settings will no longer be written for portable versions
- Renamed _Developer Tools_ category to _Development_
- Moved the following software to the _Development_ category:
  - _Go_
  - _Python 3.12.x_
  - _Python 3.13.x_
  - _Rustup_
- Added the following software:
  - _Google Drive_
  - _OneDrive_
  - _WinRAR_
  - _Skype_
  - _TeamViewer_
- _Brave_ is no longer flagged as requiring administrator privileges

# 2.0.0.0

- Completely rewritten in Python and Qt, eliminating any runtime requirement
- Updated the design of the operation window:
  - Now shows all software that will be managed with each software showing its status
- Updated first-run disclaimer
  - This will be shown to all users once more due to the change in settings management
- The software catalogue design has been updated:
  - The right-click menu has been removed
  - A button to the software's homepage has been added to the software's row
  - Icons denoting if the software requires administrator to install or if the software is contained in an archive has been added to the software's row
- Update checking will now only be performed for the non-portable version of the application
- Installable software will now be installed after it's downloaded rather than waiting for all pending software to be downloaded
- Added user settings for non-portable versions of the application:
  - Added a UI theme setting
  - Added a download timeout setting
  - Added the ability to clean up the download folder
- Added post-operation actions
- Category tabs are now sorted in alphabetical order
- Added icons to some software whose installers normally don't
- Added a new category for _.NET_ runtimes and SDKs
- Added a new category for programming languages such as _Rustup_ (Rust) and _Python_
- Added the following software:
  - _Python 3.12.x_
  - _Python 3.13.x_
  - _Qt_
  - _NVIDIA App_
  - _Streamlabs Desktop_
  - _Microsoft Visual C++ 2015-2022 Redistributable_
  - _Inkscape_
  - _Go_
- Updated download URL resolving for _NVIDIA GeForce Experience_
- Updated to _.NET 9.0 SDK_ to `9.0.101` (all _.NET_-related software will be updated to automatically download the latest version in a future release)

### Known Issues
- The application may briefly freeze when writing downloads to the disk, particularly if they are large

# 1.3.1.0

- Removed _.NET 7_-related programs as it is now end-of-life
- Added the following programs:
  - _.NET 6 Runtime_
  - _.NET 6 ASP.NET Core Runtime_
  - _.NET 6 SDK_
  - _.NET 8 Runtime_
  - _.NET 8 ASP.NET Core Runtime_
  - _.NET 8 SDK_
  - _.NET 9 Runtime_
  - _.NET 9 Desktop Runtime_
  - _.NET 9 ASP.NET Core Runtime_
  - _.NET 9 SDK_
  - _Logitech G HUB_
  - _PlayStation Accessories_
  - _DB Browser for SQLite_
- Updated code to use new .NET 9 features

# 1.3.0.0

- Migrated to the release version of .NET 9
- Added _Brave_
- Simplified the operation window

# 1.2.2.0

**There are no changes from the last release.**

Previous changelog:

- Added the following programs:
  - _Caesium Image Compressor_
  - _dnSpy_
  - _Elgato Stream Deck_
  - _GOG GALAXY_
  - _JetBrains Toolbox_
- Adjusted the style of selected programs

# 2024.11.04.18

**This release also serves as transitional update as the project will return to semantic versioning.**

- Added the following programs:
  - _Caesium Image Compressor_
  - _dnSpy_
  - _Elgato Stream Deck_
  - _GOG GALAXY_
  - _JetBrains Toolbox_
- Adjusted the style of selected programs

# 2024.10.20.20

- Better handle URL resolving errors
- Fixed the application not closing when it restarts with administrator privileges
- Moved _Audacity_ to the **Media** category

# 2024.10.18.23

- Updated to .NET 9 RC2
- Fixed the download URL for _Gimp_ failing to resolve in some cases
- Updated to download the new major release of _WinDirStat_
- Adjusted the back color of the operation window

# 2024.10.13.22

- Removed the following programs
  - Ryujinx
  - WinRAR
- Windows will now have rounded corners on systems that support it

# 2024.8.27.19

- Added the following programs
  - Ryujinx
- Improved the look of the operations window

# 2024.8.25.18

- Added the following programs
  - FileZilla
  - Minecraft Launcher (Legacy)
  - Overwolf
  - Parsec
  - PuTTY
  - Streamlink
  - System Informer

# 1.1.0.0 - 8/24/2024

- Added a link to create a suggestion issue
- The elevated permissions prompt will no longer display if installation is skipped
- Programs now have a background when hovering over them when unselected
- Improved theming

# 1.0.2.0 - 8/24/2024

- Added link to the GitHub repo to the about window

# 1.0.1.0 - 8/24/2024

- Finished application update notifier

# 1.0.0.0 - 8/24/2024

- Initial release!
