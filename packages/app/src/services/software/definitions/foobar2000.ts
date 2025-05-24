import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'foobar2000';
	public name = 'foobar2000';
	public category = [SoftwareCategory.Audio, SoftwareCategory.Media];
	public downloadName = 'foobar2000-x64.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'foobar2000.png';
	public homepage = 'https://foobar2000.org';

	public async resolveDownloadUrl() {
		const res = await fetch('https://foobar2000.org/download');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/foobar2000-x64_v\d+\.\d+\.\d+\.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(`https://foobar2000.org/files/${match[0]}`);
	}
}
