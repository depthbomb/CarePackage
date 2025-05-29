import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'cheat-engine';
	public name = 'Cheat Engine';
	public category = [SoftwareCategory.Gaming, SoftwareCategory.Utility];
	public downloadName = 'CheatEngine.exe';
	public shouldCacheUrl = true;
	public icon = 'cheat-engine.png';
	public homepage = 'https://cheatengine.org';

	public async resolveDownloadUrl() {
		const res = await fetch('https://cheatengine.org/downloads.php');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/\w{13,}\.cloudfront\.net\/installer\/\d+\/\d+/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
