import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'overwolf';
	public name = 'Overwolf';
	public category = [SoftwareCategory.Gaming];
	public downloadName = 'OverwolfSetup.zip';
	public isArchive = true;
	public shouldCacheUrl = true;
	public icon = 'overwolf.png';
	public homepage = 'https://overwolf.com';

	public async resolveDownloadUrl() {
		const res = await fetch('https://content.overwolf.com/downloads/setup/latest/regular.html');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/setup-overwolf-com\.akamaized\.net\/\d+\.\d+\.\d+\.\d+\/OverwolfSetup\.zip/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
