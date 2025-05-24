import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'keepass';
	public name = 'KeePass';
	public category = [SoftwareCategory.Security];
	public downloadName = 'KeePass-Setup.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'keepass.png';
	public homepage = 'https://keepass.info';

	public async resolveDownloadUrl() {
		const downloadPageUrl = await this.getDownloadPageUrl();
		if (!downloadPageUrl) {
			return err(DownloadUrlResolveError.Generic);
		}

		const res = await fetch(downloadPageUrl);
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/<a href="(.*)" rel="nofollow">/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[1]);
	}

	private async getDownloadPageUrl() {
		const res = await fetch('https://keepass.info/download.html');
		if (!res.ok) {
			return null;
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/sourceforge\.net\/projects\/keepass\/files\/(KeePass%202\.x\/\d+\.\d+(\.\d+)?\/KeePass-\d+\.\d+(\.\d+)?-Setup\.exe)\/download/);
		if (!match) {
			return null;
		}

		return `https://sourceforge.net/settings/mirror_choices?projectname=keepass&filename=${match[1]}&dialog=true`;
	}
}
