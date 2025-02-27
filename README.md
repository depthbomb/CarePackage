_CarePackage_ is a desktop application for Windows 10/11 heavily inspired by [Ninite](https://ninite.com/) that makes it quick and easy to download and install all of your favorite programs at once. CarePackage's intended use case is to be used on a new installation of Windows, but of course you can use it however you'd like!

You can view all software that is managed by CarePackage in [SOFTWARE.md](SOFTWARE.md).

What CarePackage **DOES**:
- Downloads the __latest__ versions of the programs you select
- Installs each program, one after another, or presents the files if the downloaded programs are compressed archives
- Allows you to opt out of installing the programs after they've been downloaded

What CarePackage **DOESN'T DO**
- Check for program updates
- Update installed programs
  - Most programs allow you to update installations by running a new installer

### Installing CarePackage

CarePackage comes in two flavors: **portable** (`carepackage.exe`) and **standalone** (`carepackage_installer.exe`). The portable version is a single executable that doesn't require any installation. Standalone, on the other hand, is installed on the system.

Functionally the two versions are the same but the standalone version will check for new releases of the application and has configurable settings.

You find the latest download with the URL: `https://bit.ly/get-carepackage`

### Planned Features

- Selecting different "versions" of software to manage, for example instead of having two listings of _Godot_ for the normal version and the C# version, it will be a single listing that lets you choose which version to manage
- The ability to text search software

### Screenshots

![The main window of CarePackage, showing the contents of the Creative tab](art/1.png "The main window of CarePackage, showing the contents of the Creative tab")
![The main window of CarePackage, showing various programs selected in the Development tab](art/2.png "The main window of CarePackage, showing various programs selected in the Development tab")
![The operation window of CarePackage, showing the pre-operation options as well as the pending programs](art/3.png "The operation window of CarePackage, showing the pre-operation options as well as the pending programs")
![The operation window of CarePackage, showing a program being downloaded while the others are pending](art/4.png "The operation window of CarePackage, showing a program being downloaded while the others are pending")
