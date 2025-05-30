import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'plex';
	public name = 'Plex';
	public category = [SoftwareCategory.Audio, SoftwareCategory.Media];
	public downloadName = '';
	public icon = 'plex-desktop.png';
	public homepage = 'https://plex.tv';

	public async resolveDownloadUrl() {
		return ok('');
	}
}
