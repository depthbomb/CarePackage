import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'nodejs-current';
	public name = 'Node.js';
	public category = [SoftwareCategory.Development, SoftwareCategory.Runtime];
	public downloadName = 'node-x64.msi';
	public shouldCacheUrl = true;
	public icon = 'nodejs.png';
	public homepage = 'https://nodejs.org';

	public async resolveDownloadUrl() {
		const res = await fetch('https://nodejs.org/dist/index.json');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const json        = await res.json() as any[];
		const { version } = json[0];

		return ok(`https://nodejs.org/dist/${version}/node-${version}-x64.msi`);
	}
}
