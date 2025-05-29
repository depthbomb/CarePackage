import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'gimp';
	public name = 'GIMP';
	public category = [SoftwareCategory.Creative];
	public downloadName = 'GimpSetup.exe';
	public shouldCacheUrl = true;
	public icon = 'gimp.png';
	public homepage = 'https://gimp.org';

	public async resolveDownloadUrl() {
		const res = await fetch('https://gimp.org/downloads');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/\/\/download\.gimp\.org\/gimp\/v\d+\.\d+\/windows\/gimp-\d+\.\d+\.\d+-setup(-\d+)?\.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(`https:${match[0]}`);
	}
}
