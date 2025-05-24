import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'razer-cortex';
	public name = 'Razer Cortex';
	public category = [SoftwareCategory.Gaming];
	public downloadName = 'RazerCortexInstaller.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = true;
	public deprecated = false;
	public icon = 'razer-cortex.png';
	public homepage = 'https://razer.com/cortex';

	public async resolveDownloadUrl() {
		return ok('https://rzr.to/cortex-download');
	}
}
