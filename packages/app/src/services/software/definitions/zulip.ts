import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'zulip';
	public name = 'Zulip';
	public category = [SoftwareCategory.Social];
	public downloadName = 'Zulip-Web-Setup.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'zulip.png';
	public homepage = 'https://zulip.com';

	public async resolveDownloadUrl() {
		return ok('https://zulip.com/apps/download/windows');
	}
}
