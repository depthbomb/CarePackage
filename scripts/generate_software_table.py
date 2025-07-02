from pathlib import Path
from src import SOFTWARE_CATALOGUE
from lib.software import SoftwareCategory

markdown_file = Path('.') / '..' / 'SOFTWARE.md'
if markdown_file.exists():
    markdown_file.unlink()

markdown = '# All Software'
markdown += '\n\nThis file was generated from `scripts/generate_software_table.py`'
markdown += '\n\n---'

for category in SoftwareCategory:
    markdown += f'\n\n## {category}'
    markdown += '\n\n|  | Name | Is Archive? | Requires Admin? | Additional Categories | # of Variants/Versions |'
    markdown += '\n| :-: | --- | :-: | :-: | :-: | :-: |'
    category_software = [sw for sw in SOFTWARE_CATALOGUE if category in sw.category]
    for software in category_software:
        icon_path = f'./resources/images/software/{software.icon}'
        is_archive = '✔️' if software.is_archive else '❌'
        requires_admin = '✔️' if software.requires_admin else '❌'
        categories = ', '.join([cat for cat in software.category if cat != category])
        markdown += f'\n| ![{software.name}]({icon_path} "{software.name}") | [{software.name}]({software.homepage}) | {is_archive} | {requires_admin} | {categories if len(categories) > 0 else 'None'} | `{len(software.variants)}` |'
    markdown += '\n\n---'

with markdown_file.open('w', encoding='utf-8') as f:
    f.write(markdown)
