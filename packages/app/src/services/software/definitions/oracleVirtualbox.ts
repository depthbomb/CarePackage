import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'oracle-virtualbox';
	public name = 'Oracle VirtualBox';
	public category = [SoftwareCategory.Utility];
	public downloadName = 'VirtualBox-Win.exe';
	public shouldCacheUrl = true;
	public requiresAdmin = true;
	public icon = 'oracle-virtualbox.png';
	public homepage = 'https://virtualbox.org';

	public async resolveDownloadUrl() {
		const res = await fetch('https://www.virtualbox.org/wiki/Downloads');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/download\.virtualbox\.org\/virtualbox\/\d+\.\d+\.\d+\/VirtualBox-\d+\.\d+\.\d+-\d{6,}-Win\.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
