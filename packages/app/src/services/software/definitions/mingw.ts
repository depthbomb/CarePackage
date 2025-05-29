import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'mingw';
	public name = 'MinGW';
	public category = [SoftwareCategory.Development];
	public downloadName = 'mingw-get-setup.exe';
	public shouldCacheUrl = true;
	public icon = 'mingw.png';
	public homepage = 'https://sourceforge.net/projects/mingw';

	public async resolveDownloadUrl() {
		const res = await fetch('https://sourceforge.net/settings/mirror_choices?projectname=mingw&filename=Installer/mingw-get-setup.exe&dialog=true');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/<a href="(.*)" rel="nofollow">/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[1]);
	}
}
