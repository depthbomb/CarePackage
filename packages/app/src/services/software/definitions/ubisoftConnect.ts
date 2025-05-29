import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'ubisoft-connect';
	public name = 'Ubisoft Connect';
	public category = [SoftwareCategory.Gaming];
	public downloadName = 'UbisoftConnectInstaller.exe';
	public requiresAdmin = true;
	public icon = 'ubisoft-connect.png';
	public homepage = 'https://ubisoft.com/en-us/ubisoft-connect';

	public async resolveDownloadUrl() {
		return ok('https://static3.cdn.ubi.com/orbit/launcher_installer/UbisoftConnectInstaller.exe');
	}
}
