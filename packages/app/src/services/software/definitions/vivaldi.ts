import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'vivaldi';
	public name = 'Vivaldi';
	public category = [SoftwareCategory.Browser];
	public downloadName = 'Vivaldi.x64.exe';
	public shouldCacheUrl = true;
	public icon = 'vivaldi.png';
	public homepage = 'https://vivaldi.com';

	public async resolveDownloadUrl() {
		const res = await fetch('https://vivaldi.com/download');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/class="download-button download-link" href="(https:\/\/downloads\.vivaldi\.com\/stable\/Vivaldi\.\d+\.\d+\.\d+\.\d+\.x64\.exe)"/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[1]);
	}
}
