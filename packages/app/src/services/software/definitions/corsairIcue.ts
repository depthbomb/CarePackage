import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'corsair-icue';
	public name = 'Corsair iCUE';
	public category = [SoftwareCategory.Peripheral];
	public downloadName = 'Install_iCue.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = true;
	public deprecated = false;
	public icon = 'corsair-icue.png';
	public homepage = 'https://corsair.com/us/en/s/icue';

	public async resolveDownloadUrl() {
		return ok('https://www3.corsair.com/software/CUE_V5/public/modules/windows/installer/Install%20iCUE.exe');
	}
}
