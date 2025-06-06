import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'discord';
	public name = 'Discord';
	public category = [SoftwareCategory.Social];
	public downloadName = '';
	public icon = 'discord.png';
	public homepage = 'https://discord.com';

	public async resolveDownloadUrl() {
		return ok('');
	}
}
