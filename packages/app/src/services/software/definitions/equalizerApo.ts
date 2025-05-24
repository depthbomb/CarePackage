import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'equalizer-apo';
	public name = 'Equalizer APO';
	public category = [SoftwareCategory.Audio, SoftwareCategory.Utility];
	public downloadName = 'EqualizerAPO-x64.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = true;
	public deprecated = false;
	public icon = 'equalizer-apo.png';
	public homepage = 'https://sourceforge.net/projects/equalizerapo';

	public async resolveDownloadUrl() {
		const res = await fetch('https://sourceforge.net/projects/equalizerapo/files/latest/download');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		return ok(res.url);
	}
}
