import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'playnite';
	public name = 'Playnite';
	public category = [SoftwareCategory.Gaming];
	public downloadName = 'PlayniteInstaller.exe';
	public icon = 'playnite.png';
	public homepage = 'https://playnite.link';

	public async resolveDownloadUrl() {
		return ok('https://playnite.link/download/PlayniteInstaller.exe');
	}
}
