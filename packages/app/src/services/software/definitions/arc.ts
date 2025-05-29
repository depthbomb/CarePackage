import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'arc';
	public name = 'Arc';
	public category = [SoftwareCategory.Browser];
	public downloadName = 'ArcInstaller.exe';
	public icon = 'arc.png';
	public homepage = 'https://arc.net';

	public async resolveDownloadUrl() {
		return ok('https://releases.arc.net/windows/ArcInstaller.exe');
	}
}
