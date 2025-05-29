import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'bitwarden-desktop';
	public name = 'Bitwarden';
	public category = [SoftwareCategory.Security];
	public downloadName = 'Bitwarden-Installer.exe';
	public icon = 'bitwarden.png';
	public homepage = 'https://bitwarden.com';

	public async resolveDownloadUrl() {
		return ok('https://vault.bitwarden.com/download/?app=desktop&platform=windows&variant=exe');
	}
}
