import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'go';
	public name = 'Go';
	public category = [SoftwareCategory.Development];
	public downloadName = 'go.windows-amd64.msi';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'go.png';
	public homepage = 'https://go.dev';

	public async resolveDownloadUrl() {
		const res = await fetch('https://go.dev/dl');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/"(\/dl\/go.*windows-amd64\.msi)"/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(`https://go.dev${match[1]}`);
	}
}
