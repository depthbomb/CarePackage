#define MyAppName "CarePackage"
#define MyAppDescription "Software Management Tool"
#define MyAppVersion "4.3.4.0"
#define MyAppPublisher "Caprine Logic"
#define MyAppExeName "carepackage.exe"
#define MyAppCopyright "Copyright (C) 2024-2025 Caprine Logic"

[Setup]
AppId={{74749A6F-089B-43D0-A213-C8F4258F8FF6}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL=https://github.com/depthbomb
AppSupportURL=https://github.com/depthbomb/CarePackage/issues/new/choose
AppUpdatesURL=https://github.com/depthbomb/CarePackage/releases
AppCopyright={#MyAppCopyright}
VersionInfoVersion={#MyAppVersion}
DefaultDirName={autopf}\{#MyAppPublisher}\{#MyAppName}
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
WizardStyle=modern
WizardResizable=no
WizardImageFile=.\images\Image_*.bmp
WizardSmallImageFile=.\images\SmallImage_*.bmp
ArchitecturesAllowed=x64compatible
UninstallDisplayIcon={app}\carepackage.exe
UninstallDisplayName={#MyAppName}
ShowTasksTreeLines=True
AlwaysShowDirOnReadyPage=True
VersionInfoCompany={#MyAppPublisher}
VersionInfoCopyright={#MyAppCopyright}
VersionInfoProductName={#MyAppName}
VersionInfoProductVersion={#MyAppVersion}
VersionInfoProductTextVersion={#MyAppVersion}
VersionInfoDescription={#MyAppDescription}

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
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall shellexec skipifsilent; Check: FromUpdate
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall shellexec skipifsilent unchecked; Check: FromNormal

[UninstallDelete]
Type: dirifempty; Name: "{app}"
