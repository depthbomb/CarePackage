import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'waterfox';
	public name = 'Waterfox';
	public category = [SoftwareCategory.Browser];
	public downloadName = 'Waterfox Setup.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'waterfox.png';
	public homepage = 'https://waterfox.net';

	public async resolveDownloadUrl() {
		const res = await fetch('https://waterfox.net/download');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/cdn\d+\.waterfox\.net\/waterfox\/releases\/\d+\.\d+\.\d+\/WINNT_x86_64\/Waterfox%20Setup%20.*\.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
