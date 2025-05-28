import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'nodejs-lts';
	public name = 'Node.js (LTS)';
	public category = [SoftwareCategory.Development, SoftwareCategory.Runtime];
	public downloadName = 'node-lts-x64.msi';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'nodejs.png';
	public homepage = 'https://nodejs.org';

	public async resolveDownloadUrl() {
		const res = await fetch('https://nodejs.org/dist/index.json');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const json        = await res.json() as any[];
		const { version } = json.find(r => r.lts !== false);

		return ok(`https://nodejs.org/dist/${version}/node-${version}-x64.msi`);
	}
}
