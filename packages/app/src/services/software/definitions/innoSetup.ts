import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'inno-setup';
	public name = 'Inno Setup';
	public category = [SoftwareCategory.Development];
	public downloadName = 'innosetup.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'inno-setup.png';
	public homepage = 'https://jrsoftware.org/isinfo.php';

	public async resolveDownloadUrl() {
		return ok('https://jrsoftware.org/download.php/is.exe?site=1');
	}
}
