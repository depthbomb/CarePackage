import { ok, err } from 'neverthrow';
import { DownloadUrlResolveError, SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'aimp';
	public name = 'AIMP';
	public category = [SoftwareCategory.Audio, SoftwareCategory.Media];
	public downloadName = 'aimp_w64.exe';
	public shouldCacheUrl = true;
	public icon = 'aimp.png';
	public homepage = 'https://aimp.ru';

	public async resolveDownloadUrl() {
		const res = await fetch('https://www.aimp.ru/?do=download.file&id=3');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		return ok(res.url);
	}
}
