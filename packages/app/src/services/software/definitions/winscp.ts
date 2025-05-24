import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'winscp';
	public name = 'WinSCP';
	public category = [
		SoftwareCategory.Network,
		SoftwareCategory.Utility,
	];
	public downloadName = 'WinSCP-Setup.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'winscp.png';
	public homepage = 'https://winscp.net';

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
		const downloadUrlPattern = /href="(https:\/\/cdn\.winscp\.net\/files\/WinSCP-.*-Setup\.exe\?secure=.*,\d{10,})"/;
		const match              = text.match(downloadUrlPattern);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[1]);
	}

	private async getDownloadPageUrl() {
		const res = await fetch('https://winscp.net/eng/download.php');
		if (!res.ok) {
			return null;
		}

		const html  = await res.text();
		const match = html.match(/\/download\/WinSCP-.*-Setup\.exe\/download/);
		if (!match) {
			return null;
		}

		return `https://winscp.net${match[0]}`;
	}
}
