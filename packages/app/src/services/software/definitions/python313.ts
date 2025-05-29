import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'python-313';
	public name = 'Python 3.13.x';
	public category = [SoftwareCategory.Development];
	public downloadName = 'python3.13.x-amd64.exe';
	public shouldCacheUrl = true;
	public icon = 'python.png';
	public homepage = 'https://python.org';

	public async resolveDownloadUrl() {
		const res = await fetch('https://python.org/api/v2/downloads/release');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const releases = await res.json() as Array<{ name: string; version: number; is_latest: boolean; }>;
		const latestV3 = releases.find(r => r.is_latest === true && r.version === 3);
		if (!latestV3) {
			return err(DownloadUrlResolveError.Generic);
		}

		const version = latestV3.name.split(' ')[1];

		return ok(`https://www.python.org/ftp/python/${version}/python-${version}-amd64.exe`);
	}
}
