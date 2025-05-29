import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'cpuz';
	public name = 'CPU-Z (Classic)';
	public category = [SoftwareCategory.Utility];
	public downloadName = 'cpu-z.exe';
	public shouldCacheUrl = true;
	public icon = 'cpuz.png';
	public homepage = 'https://cpuid.com/softwares/cpu-z.html';

	public async resolveDownloadUrl() {
		const res = await fetch(this.homepage);
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/(\d\.\d+)-en\.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(`https://download.cpuid.com/cpu-z/cpu-z_${match[1]}-en.exe`);
	}
}
