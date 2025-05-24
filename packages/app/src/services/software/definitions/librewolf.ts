import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'librewolf';
	public name = 'LibreWolf';
	public category = [SoftwareCategory.Browser];
	public downloadName = 'librewolf-windows-x86_64-setup.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = true;
	public deprecated = false;
	public icon = 'librewolf.png';
	public homepage = 'https://librewolf.net';

	public async resolveDownloadUrl() {
		const res = await fetch('https://librewolf.net/installation/windows');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/"(https:\/\/gitlab.com\/api\/v4\/projects\/\d{8}\/packages\/generic\/librewolf\/.*\/librewolf-.*-windows-x86_64-setup\.exe)"/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[1]);
	}
}
