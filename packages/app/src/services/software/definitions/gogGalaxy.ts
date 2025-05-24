import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'gog-galaxy';
	public name = 'GOG Galaxy';
	public category = [SoftwareCategory.Gaming];
	public downloadName = 'GOG_Galaxy_2.0.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'gog-galaxy.png';
	public homepage = 'https://gog.com/galaxy';

	public async resolveDownloadUrl() {
		return ok('https://webinstallers.gog-statics.com/download/GOG_Galaxy_2.0.exe');
	}
}
