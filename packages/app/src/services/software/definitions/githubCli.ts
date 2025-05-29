import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'github-cli';
	public name = 'GitHub CLI';
	public category = [SoftwareCategory.Development];
	public downloadName = 'gh_windows_amd64.msi';
	public shouldCacheUrl = true;
	public icon = 'github.png';
	public homepage = 'https://cli.github.com';

	public async resolveDownloadUrl() {
		const res = await fetch('https://cli.github.com');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/github.com\/cli\/cli\/releases\/download\/v.*\/gh_.*_windows_amd64\.msi/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
