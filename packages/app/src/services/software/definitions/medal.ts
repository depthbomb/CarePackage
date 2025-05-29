import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'medal';
	public name = 'Medal';
	public category = [SoftwareCategory.Gaming, SoftwareCategory.Social];
	public downloadName = 'MedalSetup.exe';
	public icon = 'medal.png';
	public homepage = 'https://medal.tv';

	public async resolveDownloadUrl() {
		return ok('https://install.medal.tv');
	}
}
