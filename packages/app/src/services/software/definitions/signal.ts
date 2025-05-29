import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'signal-desktop';
	public name = 'Signal';
	public category = [SoftwareCategory.Social];
	public downloadName = 'signal-desktop-win.exe';
	public shouldCacheUrl = true;
	public icon = 'signal.png';
	public homepage = 'https://signal.org';

	public async resolveDownloadUrl() {
		const res = await fetch('https://updates.signal.org/desktop/latest.yml');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/signal-desktop-win-\d+\.\d+\.\d+\.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(`https://updates.signal.org/desktop/${match[0]}`);
	}
}
