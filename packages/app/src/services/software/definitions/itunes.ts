import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'itunes';
	public name = 'iTunes';
	public category = [SoftwareCategory.Audio, SoftwareCategory.Media];
	public downloadName = 'iTunes64Setup.exe';
	public icon = 'itunes.png';
	public homepage = 'https://apple.com/itunes';

	public async resolveDownloadUrl() {
		return ok('https://www.apple.com/itunes/download/win64');
	}
}
