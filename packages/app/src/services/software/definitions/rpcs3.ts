import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'rpcs3';
	public name = 'RPCS3';
	public category = [SoftwareCategory.Emulation, SoftwareCategory.Gaming];
	public downloadName = 'rpcs3-build-win64.7z';
	public isArchive = true;
	public shouldCacheUrl = true;
	public icon = 'rpcs3.png';
	public homepage = 'https://rpcs3.net';

	public async resolveDownloadUrl() {
		const res = await fetch('https://rpcs3.net/download');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/github.com\/RPCS3\/rpcs3-binaries-win\/releases\/download\/build-[a-fA-F0-9]{40}\/rpcs3-v\d+.\d+.\d+-\d+-[a-fA-F0-9]{8}_win64.7z/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
