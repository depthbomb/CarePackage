import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'qt-oss';
	public name = 'Qt';
	public category = [SoftwareCategory.Development];
	public downloadName = 'qt-online-installer-windows-x64.exe';
	public shouldCacheUrl = true;
	public icon = 'qt.png';
	public homepage = 'https://qt.io/download-open-source';

	public async resolveDownloadUrl() {
		const res = await fetch('https://qt.io/download-qt-installer-oss');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/id="download-windows_x64" href="(.*)"/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[1]);
	}
}
