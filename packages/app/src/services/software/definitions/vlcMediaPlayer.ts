import { ok, err } from 'neverthrow';
import { BROWSER_USER_AGENT } from '~/constants';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'vlc-media-player';
	public name = 'VLC Media Player';
	public category = [SoftwareCategory.Audio, SoftwareCategory.Media];
	public downloadName = 'vlc-win64.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = true;
	public deprecated = false;
	public icon = 'vlc-media-player.png';
	public homepage = 'https://videolan.org';

	public async resolveDownloadUrl() {
		const downloadPageUrl = await this.getDownloadPageUrl();
		if (!downloadPageUrl) {
			return err(DownloadUrlResolveError.Generic);
		}

		const res = await fetch(downloadPageUrl, {
			headers: {
				'user-agent': BROWSER_USER_AGENT
			}
		});
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/URL=\'(.*)\'"/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[1]);
	}

	private async getDownloadPageUrl() {
		const res = await fetch('https://www.videolan.org/');
		if (!res.ok) {
			return null;
		}

		const html  = await res.text();
		const match = html.match(/\/\/get\.videolan\.org\/vlc\/\d+\.\d+\.\d+\/win64\/vlc-\d+\.\d+\.\d+-win64\.exe/);
		if (!match) {
			return null;
		}

		return `https:${match[0]}`;
	}
}
