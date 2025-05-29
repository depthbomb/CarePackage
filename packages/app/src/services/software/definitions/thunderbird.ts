import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'thunderbird';
	public name = 'Thunderbird';
	public category = [SoftwareCategory.Productivity, SoftwareCategory.Social];
	public downloadName = 'Thunderbird_Setup.exe';
	public shouldCacheUrl = true;
	public icon = 'thunderbird.png';
	public homepage = 'https://thunderbird.net';

	public async resolveDownloadUrl() {
		const res = await fetch('https://thunderbird.net');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/download\.mozilla\.org\/\?product=thunderbird-(.*)-SSL&os=win64&lang=en-US/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
