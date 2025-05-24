import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'opera';
	public name = 'Opera';
	public category = [SoftwareCategory.Browser];
	public downloadName = 'OperaSetup.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'opera.png';
	public homepage = 'https://opera.com';

	public async resolveDownloadUrl() {
		return ok('https://net.geo.opera.com/opera/stable/windows');
	}
}
