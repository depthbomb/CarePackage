import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'putty';
	public name = 'PuTTY';
	public category = [SoftwareCategory.Network];
	public downloadName = 'putty-64bit-installer.msi';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'putty.png';
	public homepage = 'https://putty.org';

	public async resolveDownloadUrl() {
		const res = await fetch('https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/the\.earth\.li\/~sgtatham\/putty\/latest\/w64\/putty-64bit-\d+\.\d+-installer\.msi/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
