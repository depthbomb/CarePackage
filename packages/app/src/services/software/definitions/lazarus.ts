import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'lazarus';
	public name = 'Lazarus';
	public category = [SoftwareCategory.Development];
	public downloadName = 'lazarus-fpc-win64.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'lazarus.png';
	public homepage = 'https://lazarus-ide.org';

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
		const res = await fetch('https://www.lazarus-ide.org/index.php?page=downloads');
		if (!res.ok) {
			return null;
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/sourceforge\.net\/projects\/lazarus\/files\/(Lazarus%20Windows%2064%20bits\/Lazarus%20\d+\.\d+\/lazarus-\d+\.\d+-fpc-\d+\.\d+\.\d+-win64.exe)\/download/);
		if (!match) {
			return null;
		}

		return `https://sourceforge.net/settings/mirror_choices?projectname=lazarus&filename=${match[1]}&dialog=true`;
	}
}
