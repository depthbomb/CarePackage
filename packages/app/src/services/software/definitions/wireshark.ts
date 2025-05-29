import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'wireshark';
	public name = 'Wireshark';
	public category = [SoftwareCategory.Network, SoftwareCategory.Utility];
	public downloadName = 'Wireshark-x64.exe';
	public shouldCacheUrl = true;
	public requiresAdmin = true;
	public icon = 'wireshark.png';
	public homepage = 'https://wireshark.org';

	public async resolveDownloadUrl() {
		const res = await fetch('https://wireshark.org');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/\d+.na.dl.wireshark.org\/win64\/Wireshark-\d+.\d+.\d+-x64.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
