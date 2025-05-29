import { ok, err } from 'neverthrow';
import { DownloadUrlResolveError, SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'inno-setup';
	public name = 'Inno Setup';
	public category = [SoftwareCategory.Development];
	public downloadName = 'innosetup.exe';
	public shouldCacheUrl = true;
	public icon = 'inno-setup.png';
	public homepage = 'https://jrsoftware.org/isinfo.php';

	public async resolveDownloadUrl() {
		const res = await fetch('https://jrsoftware.org/download.php/is.exe?site=1');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		return ok(res.url);
	}
}
