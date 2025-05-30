import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'plexamp';
	public name = 'Plexamp';
	public category = [SoftwareCategory.Audio, SoftwareCategory.Media];
	public downloadName = 'Plexamp Setup.exe';
	public shouldCacheUrl = true;
	public icon = 'plexamp.png';
	public homepage = 'https://plex.tv';
	public parent = 'plex';

	public async resolveDownloadUrl() {
		const res = await fetch('https://www.plex.tv/wp-json/plex/v1/downloads/plexamp');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/Plexamp%20Setup%20\d+\.\d+\.\d+\.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(`https://plexamp.plex.tv/plexamp.plex.tv/desktop/${match[0]}`);
	}
}
