from pathlib import Path
from src import SOFTWARE_CATALOGUE

markdown_file = Path('.') / '..' / 'SOFTWARE.md'
if markdown_file.exists():
    markdown_file.unlink()

markdown = '# All Software'
markdown += '\n\nThis file was generated from `scripts/generate_software_table.py`'
markdown += '\n\n---'

for (category, software_list) in SOFTWARE_CATALOGUE.items():
    markdown += f'\n\n## {category}'
    markdown += '\n\n|  | Name | Homepage | Is Archive? | Requires Admin? |'
    markdown += '\n| :-: | --- | --- | :-: | :-: |'
    for software in software_list:
        icon_path = f'./resources/images/software/{software.icon}'
        is_archive = '✔️' if software.is_archive else '❌'
        requires_admin = '✔️' if software.requires_admin else '❌'
        markdown += f'\n| ![{software.name}]({icon_path} "{software.name}") | {software.name} | [{software.homepage}]({software.homepage}) | {is_archive} | {requires_admin} |'
    markdown += '\n\n---'

with markdown_file.open('w') as f:
    f.write(markdown)
