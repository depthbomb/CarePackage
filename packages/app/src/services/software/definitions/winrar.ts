import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'winrar';
	public name = 'WinRAR';
	public category = [SoftwareCategory.FileManagement, SoftwareCategory.Utility];
	public downloadName = 'WinRAR.exe';
	public shouldCacheUrl = true;
	public icon = 'winrar.png';
	public homepage = 'https://win-rar.com';

	public async resolveDownloadUrl() {
		const res = await fetch('https://win-rar.com/download.html?&L=0');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/"(\/fileadmin\/winrar-versions\/downloader\/WinRAR-\d{2,}\.exe)"/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(`https://win-rar.com${match[1]}`);
	}
}
