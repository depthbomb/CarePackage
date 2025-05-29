import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'lightshot';
	public name = 'Lightshot';
	public category = [SoftwareCategory.Media, SoftwareCategory.Utility];
	public downloadName = 'setup-lightshot.exe';
	public icon = 'lightshot.png';
	public homepage = 'https://app.prntscr.com';

	public async resolveDownloadUrl() {
		return ok('https://app.prntscr.com/build/setup-lightshot.exe');
	}
}
