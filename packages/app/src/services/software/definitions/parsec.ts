import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'parsec';
	public name = 'Parsec';
	public category = [SoftwareCategory.Gaming];
	public downloadName = 'parsec-windows.exe';
	public requiresAdmin = true;
	public icon = 'parsec.png';
	public homepage = 'https://parsec.app';

	public async resolveDownloadUrl() {
		return ok('https://builds.parsec.app/package/parsec-windows.exe');
	}
}
