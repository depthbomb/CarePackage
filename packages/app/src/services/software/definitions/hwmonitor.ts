import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'hwmonitor';
	public name = 'HWMonitor';
	public category = [SoftwareCategory.Utility];
	public downloadName = 'hwmonitor.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'hwmonitor.png';
	public homepage = 'https://cpuid.com/softwares/hwmonitor.html';

	public async resolveDownloadUrl() {
		const res = await fetch(this.homepage);
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/(\d\.\d+)\.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(`https://download.cpuid.com/hwmonitor/hwmonitor_${match[1]}.exe`);
	}
}
