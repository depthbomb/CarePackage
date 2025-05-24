import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'mozilla-firefox';
	public name = 'Mozilla Firefox';
	public category = [SoftwareCategory.Browser];
	public downloadName = 'Firefox Installer.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'mozilla-firefox.png';
	public homepage = 'https://mozilla.org/firefox';

	public async resolveDownloadUrl() {
		return ok('https://download.mozilla.org/?product=firefox-latest-ssl&os=win64&lang=en-US');
	}
}
