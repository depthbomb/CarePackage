import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'krita';
	public name = 'Krita';
	public category = [SoftwareCategory.Creative];
	public downloadName = 'krita-x64-setup.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'krita.png';
	public homepage = 'https://krita.org';

	public async resolveDownloadUrl() {
		const res = await fetch('https://krita.org/en/download');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/download\.kde\.org\/stable\/krita\/\d+\.\d+\.\d+\/krita-x64-\d+\.\d+\.\d+-setup\.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
