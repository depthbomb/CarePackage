import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'defraggler';
	public name = 'Defraggler';
	public category = [SoftwareCategory.FileManagement, SoftwareCategory.Utility];
	public downloadName = 'dfsetup.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = true;
	public deprecated = false;
	public icon = 'defraggler.png';
	public homepage = 'https://ccleaner.com/defraggler';

	public async resolveDownloadUrl() {
		const downloadPageUrl = await this.getDownloadPageUrl();
		if (!downloadPageUrl) {
			return err(DownloadUrlResolveError.Generic);
		}

		const res = await fetch(downloadPageUrl);
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const text               = await res.text();
		const downloadUrlPattern = /https:\/\/download\.ccleaner\.com\/dfsetup(\d){2,3}\.exe/;
		const match              = text.match(downloadUrlPattern);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}

	private async getDownloadPageUrl() {
		const res = await fetch('https://ccleaner.com/defraggler/download/standard');
		if (!res.ok) {
			return null;
		}

		const html  = await res.text();
		const match = html.match(/\/en-us\/api\/modular-page\?guid=[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}/);
		if (!match) {
			return null;
		}

		return `https://www.ccleaner.com${match[0]}`;
	}
}
