import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'joplin';
	public name = 'Joplin';
	public category = [SoftwareCategory.Productivity];
	public downloadName = 'Joplin-Setup.exe';
	public shouldCacheUrl = true;
	public icon = 'joplin.png';
	public homepage = 'https://joplinapp.org';

	public async resolveDownloadUrl() {
		const res = await fetch('https://joplinapp.org/download');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/objects.joplinusercontent.com\/v\d+.\d+.\d+\/Joplin-Setup-\d+.\d+.\d+.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
