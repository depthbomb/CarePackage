import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'itch';
	public name = 'itch';
	public category = [SoftwareCategory.Gaming];
	public downloadName = 'itch-setup.exe';
	public icon = 'itch.png';
	public homepage = 'https://itch.io/app';

	public async resolveDownloadUrl() {
		return ok('https://itch.io/app/download');
	}
}
