import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'streamlabs-desktop';
	public name = 'Streamlabs Desktop';
	public category = [SoftwareCategory.Media];
	public downloadName = 'Streamlabs+Desktop+Setup.exe';
	public requiresAdmin = true;
	public icon = 'streamlabs-desktop.png';
	public homepage = 'https://streamlabs.com/streamlabs-live-streaming-software';

	public async resolveDownloadUrl() {
		const res = await fetch('https://streamlabs.com/streamlabs-desktop/download?sdb=0');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		return ok(res.url);
	}
}
