import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'ea-app';
	public name = 'EA App';
	public category = [SoftwareCategory.Gaming];
	public downloadName = 'EAappInstaller.exe';
	public icon = 'ea-app.png';
	public homepage = 'https://ea.com/ea-app';

	public async resolveDownloadUrl() {
		return ok('https://origin-a.akamaihd.net/EA-Desktop-Client-Download/installer-releases/EAappInstaller.exe');
	}
}
