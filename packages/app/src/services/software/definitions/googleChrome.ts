import { ok, err } from 'neverthrow';
import { randomUUID } from 'node:crypto';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'google-chrome';
	public name = 'Google Chrome';
	public category = [SoftwareCategory.Browser];
	public downloadName = 'ChromeSetup.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'google-chrome.png';
	public homepage = 'https://google.com/chrome';

	public async resolveDownloadUrl() {
		const res = await fetch('https://www.google.com/chrome/static/js/installer.min.js');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/stablechannel:"([{(]?[0-9A-F]{8}-?(?:[0-9A-F]{4}-?){3}[0-9A-F]{12}[)}]?)"/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		const iid     = `{${randomUUID()}}`;
		const appGuid = match[1];
		const path    = encodeURIComponent(`appguid=${appGuid}&iid=${iid}&lang=en&browser=4&usagestats=0&appname=Google%20Chrome&needsadmin=prefers&ap=x64-statsdef_1&`);

		return ok(`https://dl.google.com/tag/s/${path}installdataindex=empty/update2/installers/ChromeSetup.exe`);
	}
}
