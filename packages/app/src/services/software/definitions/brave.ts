import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'brave-browser';
	public name = 'Brave';
	public category = [SoftwareCategory.Browser];
	public downloadName = 'BraveBrowserSetup.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'brave-browser.png';
	public homepage = 'https://brave.net';

	public async resolveDownloadUrl() {
		return ok('https://laptop-updates.brave.com/download/desktop/release/BRV010?bitness=64');
	}
}
