import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'system-informer';
	public name = 'System Informer';
	public category = [SoftwareCategory.Utility];
	public downloadName = 'systeminformer-setup.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'system-informer.png';
	public homepage = 'https://systeminformer.sourceforge.io';

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
		const res = await fetch('https://systeminformer.sourceforge.io/downloads');
		if (!res.ok) {
			return null;
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/sourceforge\.net\/projects\/systeminformer\/files\/(systeminformer-\d+\.\d+\.\d+-release-setup\.exe)\/download/);
		if (!match) {
			return null;
		}

		return `https://sourceforge.net/settings/mirror_choices?projectname=systeminformer&filename=${match[1]}&dialog=true`;
	}
}
