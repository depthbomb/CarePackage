import ast
from typing import cast
from pathlib import Path
from hashlib import sha256
from datetime import datetime
from invoke import task, Context
from tempfile import NamedTemporaryFile

_INSTALLER_SUFFIXES = {'.exe', '.msi'}
_INSTALLER_PROFILES = {
    'Inno Setup': {
        'signatures': (b'inno setup setup data', b'inno setup'),
        'args': ['/VERYSILENT', '/SUPPRESSMSGBOXES', '/NORESTART', '/SP-'],
    },
    'NSIS': {
        'signatures': (
            b'nullsoft.nsis.exehead',
            b'nullsoft install system',
            b'nullsoftinst',
        ),
        'args': ['/S'],
    },
    'Squirrel.Windows': {
        'signatures': (
            b'squirrel.windows',
            b'squirrelsetup.log',
            'squirrel.windows'.encode('utf-16le'),
            'squirrelsetup.log'.encode('utf-16le'),
        ),
        'args': ['--silent'],
    },
    'WiX Burn': {
        'signatures': (b'wixbundleproperties', b'wixstdba'),
        'args': ['/quiet', '/norestart'],
    },
    'InstallShield': {
        'signatures': (b'installshield',),
        'args': ['/s'],
    },
}

def _installer_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    if path.is_dir():
        return sorted(
            file for file in path.iterdir()
            if file.is_file() and file.suffix.lower() in _INSTALLER_SUFFIXES
        )
    raise FileNotFoundError(f'Installer path does not exist: {path}')


def _inspect_installer(path: Path) -> tuple[str, list[str], str, str]:
    digest = sha256()
    signatures = {
        signature: engine
        for engine, profile in _INSTALLER_PROFILES.items()
        for signature in profile['signatures']
    }
    max_signature_length = max(map(len, signatures))
    detected_engines = set()
    tail = b''

    with path.open('rb') as installer:
        while chunk := installer.read(1024 * 1024):
            digest.update(chunk)
            searchable = (tail + chunk).lower()
            detected_engines.update(
                engine for signature, engine in signatures.items()
                if signature in searchable
            )
            tail = searchable[-(max_signature_length - 1):]

    if path.suffix.lower() == '.msi':
        return 'Windows Installer (MSI)', ['/qn', '/norestart'], 'high', digest.hexdigest()

    if len(detected_engines) == 1:
        engine = detected_engines.pop()
        profile = _INSTALLER_PROFILES[engine]
        confidence = 'low' if engine == 'InstallShield' else 'medium'
        return engine, cast(list[str], profile['args']), confidence, digest.hexdigest()

    if len(detected_engines) > 1:
        engines = ', '.join(sorted(detected_engines))
        return f'Ambiguous ({engines})', [], 'low', digest.hexdigest()

    return 'Unknown/custom executable', [], 'none', digest.hexdigest()


def _assignment_to_self(statement: ast.stmt, attribute: str) -> bool:
    return (
        isinstance(statement, ast.Assign) and
        any(
            isinstance(target, ast.Attribute) and
            isinstance(target.value, ast.Name) and
            target.value.id == 'self' and
            target.attr == attribute
            for target in statement.targets
        )
    )


def _definition_index() -> dict[str, list[tuple[Path, ast.Assign, ast.Assign | None]]]:
    definitions = {}
    software_dir = Path('src/lib/software')
    for path in software_dir.rglob('*.py'):
        source = path.read_bytes().decode('utf-8-sig')
        tree = ast.parse(source, filename=str(path))
        for class_node in (node for node in tree.body if isinstance(node, ast.ClassDef)):
            for init_node in (
                node for node in class_node.body
                if isinstance(node, ast.FunctionDef) and node.name == '__init__'
            ):
                assignments = [node for node in ast.walk(init_node) if isinstance(node, ast.Assign)]
                download_assignment = next(
                    (node for node in assignments if _assignment_to_self(node, 'download_name')),
                    None
                )
                if download_assignment is None:
                    continue
                try:
                    assigned_name = ast.literal_eval(download_assignment.value)
                except (TypeError, ValueError):
                    continue
                if not isinstance(assigned_name, str):
                    continue
                silent_assignment = next(
                    (node for node in assignments if _assignment_to_self(node, 'silent_install_args')),
                    None
                )
                definitions.setdefault(assigned_name.casefold(), []).append(
                    (path, download_assignment, silent_assignment)
                )
    return definitions


def _assignment_value(assignment: ast.Assign | None):
    if assignment is None:
        return None
    try:
        return ast.literal_eval(assignment.value)
    except (TypeError, ValueError):
        return '<dynamic expression>'


def _write_silent_install_args(
    path: Path,
    download_assignment: ast.Assign,
    silent_assignment: ast.Assign | None,
    args: list[str]
):
    raw_source = path.read_bytes()
    has_bom = raw_source.startswith(b'\xef\xbb\xbf')
    source = raw_source.decode('utf-8-sig')
    newline = '\r\n' if '\r\n' in source else '\n'
    lines = source.splitlines(keepends=True)
    assignment = silent_assignment or download_assignment
    assignment_line = lines[assignment.lineno - 1]
    indentation = assignment_line[:len(assignment_line) - len(assignment_line.lstrip())]
    replacement = f'{indentation}self.silent_install_args = {args!r}{newline}'

    if silent_assignment is None:
        lines.insert(download_assignment.end_lineno, replacement)
    else:
        lines[silent_assignment.lineno - 1:silent_assignment.end_lineno] = [replacement]

    encoded_source = ''.join(lines).encode('utf-8')
    if has_bom:
        encoded_source = b'\xef\xbb\xbf' + encoded_source

    temporary_path = None
    try:
        with NamedTemporaryFile(dir=path.parent, prefix=f'.{path.name}.', suffix='.tmp', delete=False) as temporary:
            temporary.write(encoded_source)
            temporary_path = Path(temporary.name)
        temporary_path.replace(path)
    finally:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)


@task(
    positional=['installer'],
    help={
        'installer': 'An installer file or a directory containing .exe and .msi installers.',
        'apply': 'Write safe suggestions to matching software definitions.',
        'force': 'Replace conflicting existing arguments; only effective with --apply.',
    }
)
def detect_silent_install_args(c: Context, installer: str, apply: bool = False, force: bool = False):
    del c
    installer_path = Path(installer).expanduser().resolve()
    files = _installer_files(installer_path)
    if not files:
        print(f'No .exe or .msi installers found in {installer_path}')
        return

    definitions = _definition_index()
    for index, file in enumerate(files):
        engine, args, confidence, digest = _inspect_installer(file)
        if index:
            print()
        print(file)
        print(f'  SHA-256:   {digest}')
        print(f'  Engine:    {engine}')
        print(f'  Confidence: {confidence}')
        if file.suffix.lower() == '.msi':
            print('  Suggested: handled automatically by CarePackage via msiexec.exe /qn /norestart')
        elif args:
            print(f'  Suggested: silent_install_args = {args!r}')
        else:
            print('  Suggested: none; consult the vendor or an exact-hash package manifest')

        if file.suffix.lower() != '.msi' and args and confidence in {'medium', 'high'}:
            matches = definitions.get(file.name.casefold(), [])
            if len(matches) == 0:
                print('  Definition: no exact download_name match')
            elif len(matches) > 1:
                matched_paths = ', '.join(str(match[0]) for match in matches)
                print(f'  Definition: ambiguous matches ({matched_paths}); skipped')
            else:
                path, download_assignment, silent_assignment = matches[0]
                current_args = _assignment_value(silent_assignment)
                print(f'  Definition: {path}')
                if current_args == args:
                    print('  Definition update: unchanged')
                elif silent_assignment is not None and not force:
                    print(f'  Definition update: conflict ({current_args!r}); use --apply --force to replace')
                elif apply:
                    _write_silent_install_args(path, download_assignment, silent_assignment, args)
                    action = 'updated' if silent_assignment is not None else 'added'
                    print(f'  Definition update: {action}')
                else:
                    action = 'replace existing value' if silent_assignment is not None else 'add assignment'
                    print(f'  Definition update: would {action}; use --apply to write')
        elif apply and file.suffix.lower() != '.msi':
            print('  Definition update: skipped because the suggestion is not safe to apply')
        print('  Warning:   review and test this result in a disposable Windows environment')

@task
def generate_qrc_resources(c: Context):
    output_path = Path('.') / 'src' / 'rc'
    output_path.mkdir(parents=True, exist_ok=True)

    resources_path = Path('.') / 'resources'
    for file in resources_path.glob('*.qrc'):
        c.run(f'pyside6-rcc {file} -o {output_path / f'{file.stem}.py'}')

@task(pre=[generate_qrc_resources])
def build(c: Context):
    from src import (
        APP_ORG,
        APP_NAME,
        APP_DESCRIPTION,
        APP_DISPLAY_NAME,
        APP_VERSION_STRING
    )
    cmd = ' '.join([
        'nuitka',
        'src',
        f'--output-dir=build --output-filename={APP_NAME}',
        '--standalone',
        '--include-package=src.lib.software',
        '--enable-plugin=pyside6 --enable-plugin=upx',
        '--onefile-no-compression',
        '--windows-uac-admin --windows-icon-from-ico=resources/icons/icon.ico --windows-console-mode=attach',
        f'--company-name="{APP_ORG}" --product-name="{APP_DISPLAY_NAME}" --product-version={APP_VERSION_STRING} --file-description="{APP_DESCRIPTION}" --copyright="Copyright (c) 2024-2026 {APP_ORG}"',
    ])
    c.run(cmd)

@task
def generate_software_table(c: Context):
    from src import SOFTWARE_CATALOGUE
    from src.lib.software import SoftwareCategory

    markdown_file = Path('.') / 'SOFTWARE.md'
    markdown_file.unlink(missing_ok=True)

    markdown = '# All Software'
    markdown += '\n\nThis file was generated from `tasks.py`'
    markdown += '\n\n---'

    for category in SoftwareCategory:
        markdown += f'\n\n## {category}'
        markdown += '\n\n|  | Name | Is Archive? | Additional Categories | # of Variants/Versions |'
        markdown += '\n| :-: | --- | :-: | :-: | :-: |'
        category_software = [sw for sw in SOFTWARE_CATALOGUE if category in sw.category]
        for software in category_software:
            icon_path = f'./resources/images/software/{software.icon}'
            is_archive = '✔️' if software.is_archive else '❌'
            categories = ', '.join([cat for cat in software.category if cat != category])
            markdown += f'\n| ![{software.name}]({icon_path} "{software.name}") | [{software.name}]({software.homepage}) | {is_archive} | {categories if len(categories) > 0 else 'None'} | `{len(software.variants)}` |'
        markdown += '\n\n---'

    with markdown_file.open('w', encoding='utf-8') as f:
        f.write(markdown)

@task
def create_setup(c: Context):
    from src import (
        APP_ORG,
        APP_NAME,
        APP_CLSID,
        APP_REPO_URL,
        APP_DESCRIPTION,
        APP_RELEASES_URL,
        APP_DISPLAY_NAME,
        APP_NEW_ISSUE_URL,
        APP_USER_MODEL_ID,
        APP_VERSION_STRING
    )
    definitions = {
        'NameLong': APP_DISPLAY_NAME,
        'Version': APP_VERSION_STRING,
        'Description': APP_DESCRIPTION,
        'Company': APP_ORG,
        'ExeName': f'{APP_NAME}.exe',
        'AppUserModelId': APP_USER_MODEL_ID,
        'AppUserModelToastActivatorClsid': APP_CLSID,
        'Copyright': f'Copyright (c) 2024-{datetime.now().year} {APP_ORG}',
        'RepoUrl': APP_REPO_URL,
        'ReleasesUrl': APP_RELEASES_URL,
        'IssuesUrl': APP_NEW_ISSUE_URL
    }
    cmd = ' '.join([
        'iscc.exe',
        'setup/setup.iss',
        ' '.join([f"/d{key}=\"{value}\"" for key, value in definitions.items()])
    ])
    c.run(cmd)

@task
def remove_unused_files(c: Context):
    build_dir = Path('.') / 'build' / 'src.dist'

    deletable_files = [
        # <root>
        build_dir / '_decimal.pyd',
        build_dir / '_hashlib.pyd',
        build_dir / '_socket.pyd',
        build_dir / '_wmi.pyd',
        build_dir / 'libcrypto-3.dll',
        build_dir / 'msvcp140.dll',
        build_dir / 'qt6pdf.dll',
        build_dir / 'qt6svg.dll',
        build_dir / 'select.pyd',
        build_dir / 'unicodedata.pyd',
        # <root>/shiboken6
        build_dir / 'shiboken6' / 'msvcp140_1.dll',
        build_dir / 'shiboken6' / 'msvcp140_2.dll',
        build_dir / 'shiboken6' / 'msvcp140_codecvt_ids.dll',
        # <root>/PySide6/qt-plugins/iconengines
        build_dir / 'PySide6' / 'qt-plugins' / 'iconengines' / 'qsvgicon.dll',
        # <root>/PySide6/qt-plugins/imageformats
        build_dir / 'PySide6' / 'qt-plugins' / 'imageformats' / 'qgif.dll',
        build_dir / 'PySide6' / 'qt-plugins' / 'imageformats' / 'qicns.dll',
        build_dir / 'PySide6' / 'qt-plugins' / 'imageformats' / 'qjpeg.dll',
        build_dir / 'PySide6' / 'qt-plugins' / 'imageformats' / 'qpdf.dll',
        build_dir / 'PySide6' / 'qt-plugins' / 'imageformats' / 'qsvg.dll',
        build_dir / 'PySide6' / 'qt-plugins' / 'imageformats' / 'qtga.dll',
        build_dir / 'PySide6' / 'qt-plugins' / 'imageformats' / 'qtiff.dll',
        build_dir / 'PySide6' / 'qt-plugins' / 'imageformats' / 'qwbmp.dll',
        build_dir / 'PySide6' / 'qt-plugins' / 'imageformats' / 'qwebp.dll',
        # <root>/PySide6/qt-plugins/platforms
        build_dir / 'PySide6' / 'qt-plugins' / 'platforms' / 'qdirect2d.dll',
        build_dir / 'PySide6' / 'qt-plugins' / 'platforms' / 'qminimal.dll',
        build_dir / 'PySide6' / 'qt-plugins' / 'platforms' / 'qoffscreen.dll',
    ]
    deletable_dirs = [
        build_dir / 'PySide6' / 'qt-plugins' / 'iconengines'
    ]

    for file in cast(list[Path], [*deletable_files, *deletable_dirs]):
        if file.is_file():
            file.unlink(missing_ok=True)
        elif file.is_dir():
            file.rmdir()

@task(pre=[build], post=[remove_unused_files, create_setup])
def deploy(c: Context):
    pass
