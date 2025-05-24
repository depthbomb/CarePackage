import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'streamlabs-desktop';
	public name = 'Streamlabs Desktop';
	public category = [SoftwareCategory.Media];
	public downloadName = 'Streamlabs+Desktop+Setup.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = true;
	public deprecated = false;
	public icon = 'streamlabs-desktop.png';
	public homepage = 'https://streamlabs.com/streamlabs-live-streaming-software';

	public async resolveDownloadUrl() {
		return ok('https://streamlabs.com/streamlabs-desktop/download?sdb=0');
	}
}
