import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'installforge';
	public name = 'InstallForge';
	public category = [SoftwareCategory.Development];
	public downloadName = 'IFSetup.exe';
	public requiresAdmin = true;
	public icon = 'installforge.png';
	public homepage = 'https://installforge.net';

	public async resolveDownloadUrl() {
		return ok('https://installforge.net/downloads/?i=IFSetup');
	}
}
