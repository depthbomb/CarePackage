# 2.2.0.0

- Renamed the _Creative Tools_ category to _Creative_
- Updated the design of the operation window:
  - Current download speed is now displayed while software is downloading
  - The download progress bar will now replace the software name when possible
  - Changed spinner style
- Update checking is now enabled for portable installations
- The operation window will now scroll to the software that has just started downloading
- Adjusted some software so that they are not flagged as requiring admin privileges
- Fixed some cases where software that errored during the installation step would now show an erroneous status
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
