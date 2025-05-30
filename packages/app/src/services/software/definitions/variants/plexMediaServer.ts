import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'plex-media-server';
	public name = 'Plex Media Server';
	public category = [SoftwareCategory.Media];
	public downloadName = 'PlexMediaServer-x86_64.exe';
	public shouldCacheUrl = true;
	public icon = 'plex-media-server.png';
	public homepage = 'https://plex.tv';
	public parent = 'plex';

	public async resolveDownloadUrl() {
		const res = await fetch('https://plex.tv/api/downloads/5.json');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/downloads\.plex\.tv\/plex-media-server-new\/\d+\.\d+\.\d+\.\d+-[a-f0-9]{9}\/windows\/PlexMediaServer-\d+\.\d+\.\d+\.\d+-[a-f0-9]{9}-x86_64\.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
