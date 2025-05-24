import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'raspberry-pi-imager';
	public name = 'Raspberry Pi Imager';
	public category = [SoftwareCategory.Utility];
	public downloadName = 'imager_latest.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = true;
	public deprecated = false;
	public icon = 'raspberry-pi-imager.png';
	public homepage = 'https://raspberrypi.com/software';

	public async resolveDownloadUrl() {
		return ok('https://downloads.raspberrypi.org/imager/imager_latest.exe');
	}
}
