import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'obs-studio';
	public name = 'OBS Studio';
	public category = [SoftwareCategory.Media];
	public downloadName = 'OBS-Studio-Windows-Installer.exe';
	public shouldCacheUrl = true;
	public requiresAdmin = true;
	public icon = 'obs-studio.png';
	public homepage = 'https://obsproject.com';

	public async resolveDownloadUrl() {
		const res = await fetch('https://obsproject.com/download');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/cdn-fastly\.obsproject\.com\/downloads\/OBS-Studio-\d+.\d+.\d+-Windows-Installer\.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
