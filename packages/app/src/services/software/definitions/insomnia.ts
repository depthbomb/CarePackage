import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'insomnia';
	public name = 'Insomnia';
	public category = [
		SoftwareCategory.Development,
		SoftwareCategory.Network,
	];
	public downloadName = 'Insomnia.Core.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'insomnia.png';
	public homepage = 'https://insomnia.rest';

	public async resolveDownloadUrl() {
		return ok('https://updates.insomnia.rest/downloads/windows/latest?app=com.insomnia.app&source=website');
	}
}
