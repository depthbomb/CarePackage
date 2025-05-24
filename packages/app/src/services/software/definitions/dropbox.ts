import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'dropbox';
	public name = 'Dropbox';
	public category = [SoftwareCategory.FileManagement, SoftwareCategory.Utility];
	public downloadName = 'DropoboxInstaller.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'dropbox.png';
	public homepage = 'https://dropbox.com';

	public async resolveDownloadUrl() {
		return ok('https://www.dropbox.com/download?os=win&plat=win');
	}
}
