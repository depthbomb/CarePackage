import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'telegram-desktop';
	public name = 'Telegram';
	public category = [SoftwareCategory.Social];
	public downloadName = 'tsetup.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'telegram.png';
	public homepage = 'https://telegram.org';

	public async resolveDownloadUrl() {
		return ok('https://telegram.org/dl/desktop/win64');
	}
}
