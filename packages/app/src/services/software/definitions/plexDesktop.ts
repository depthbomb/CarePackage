import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'plex-desktop';
	public name = 'Plex Desktop';
	public category = [SoftwareCategory.Media];
	public downloadName = 'Plex-x86_64.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'plex-desktop.png';
	public homepage = 'https://plex.tv';

	public async resolveDownloadUrl() {
		const res = await fetch('https://plex.tv/api/downloads/6.json');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/downloads\.plex\.tv\/plex-desktop\/\d+\.\d+\.\d+\.\d+-[a-f0-9]{8}\/windows\/Plex-\d+\.\d+\.\d+\.\d+-[a-f0-9]{8}-x86_64\.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
