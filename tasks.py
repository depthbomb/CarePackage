from pathlib import Path
from invoke import task, Context

@task
def build(c: Context):
    from src import APP_VERSION_STRING

    cmd = ' '.join([
        'nuitka',
        'src',
        '--output-dir=build --output-filename=carepackage',
        '--standalone',
        '--enable-plugin=pyside6 --enable-plugin=upx',
        '--onefile-no-compression',
        '--windows-uac-admin --windows-icon-from-ico=resources/icons/icon.ico --windows-console-mode=attach',
        f'--company-name="Caprine Logic" --product-name="CarePackage" --product-version={APP_VERSION_STRING} --file-description="Software Management Tool" --copyright="Copyright (c) 2024-2025 Caprine Logic"',
    ])
    c.run(cmd)

@task
def generate_qrc_resources(c: Context):
    output_path = Path('.') / 'src' / 'rc'
    output_path.mkdir(parents=True, exist_ok=True)

    c.run(f'pyside6-rcc resources/images.qrc -o {output_path / 'images.py'}')
    c.run(f'pyside6-rcc resources/icons.qrc -o {output_path / 'icons.py'}')

@task
def generate_software_table(c: Context):
    from pathlib import Path
    from src import SOFTWARE_CATALOGUE
    from src.lib.software import SoftwareCategory

    markdown_file = Path('.') / 'SOFTWARE.md'
    markdown_file.unlink(missing_ok=True)

    markdown = '# All Software'
    markdown += '\n\nThis file was generated from `scripts/generate_software_table.py`'
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
