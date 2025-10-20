[Setup]
AppId={{74749A6F-089B-43D0-A213-C8F4258F8FF6}
AppName={#NameLong}
AppVersion={#Version}
AppVerName={#NameLong} {#Version}
AppPublisher={#Company}
AppPublisherURL={#RepoUrl}
AppSupportURL={#IssuesUrl}
AppUpdatesURL={#ReleasesUrl}
AppCopyright={#Copyright}
VersionInfoVersion={#Version}
DefaultDirName={autopf}\{#Company}\{#NameLong}
DisableDirPage=yes
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
AllowNoIcons=yes
LicenseFile=..\LICENSE
OutputDir=..\build
OutputBaseFilename=carepackage_installer
SetupIconFile=..\resources\icons\icon.ico
Compression=lzma2/ultra64
SolidCompression=yes
ArchitecturesAllowed=x64compatible
MinVersion=10.0
WizardStyle=modern
WizardResizable=no
ShowTasksTreeLines=yes
WizardImageFile=.\images\Image_*.bmp
WizardSmallImageFile=.\images\SmallImage_*.bmp
UninstallDisplayIcon={app}\{#ExeName}
UninstallDisplayName={#NameLong} - {#Description}
VersionInfoCompany={#Company}
VersionInfoCopyright={#Copyright}
VersionInfoProductName={#NameLong}
VersionInfoProductVersion={#Version}
VersionInfoProductTextVersion={#Version}
VersionInfoDescription={#Description}

[Code]
function FromUpdate: Boolean;
begin
	Result := ExpandConstant('{param:update|no}') = 'yes'
end;

function FromNormal: Boolean;
begin
	Result := FromUpdate = False
end;

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}";

[Files]
Source: "..\build\src.dist\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs
Source: "..\LICENSE"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\CHANGELOG.md"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\resources\carepackage.VisualElementsManifest.xml"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\resources\Square70x70Logo.png"; DestDir: "{app}"; Flags: ignoreversion
Source: "..\resources\Square150x150Logo.png"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\{#Company}\{#NameLong}"; Filename: "{app}\{#ExeName}"; AppUserModelID: "{#AppUserModelId}"; AppUserModelToastActivatorCLSID: "{#AppUserModelToastActivatorClsid}"
Name: "{autodesktop}\{#NameLong}"; Filename: "{app}\{#ExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#ExeName}"; Description: "{cm:LaunchProgram,{#StringChange(NameLong, '&', '&&')}}"; Flags: nowait postinstall shellexec skipifsilent; Check: FromUpdate
Filename: "{app}\{#ExeName}"; Description: "{cm:LaunchProgram,{#StringChange(NameLong, '&', '&&')}}"; Flags: nowait postinstall shellexec skipifsilent unchecked; Check: FromNormal

[UninstallDelete]
Type: dirifempty; Name: "{app}"
