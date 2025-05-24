import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'jetbrains-toolbox';
	public name = 'JetBrains Toolbox';
	public category = [SoftwareCategory.Development];
	public downloadName = 'jetbrains-toolbox.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'jetbrains-toolbox.png';
	public homepage = 'https://jetbrains.com/toolbox-app';

	public async resolveDownloadUrl() {
		const res = await fetch('https://data.services.jetbrains.com/products/releases?code=TBA&latest=true&type=release');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/download\.jetbrains\.com\/toolbox\/jetbrains-toolbox-\d+\.\d+\.\d+\.\d+\.exe\b/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
