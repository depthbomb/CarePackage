import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'sublime-text';
	public name = 'Sublime Text';
	public category = [SoftwareCategory.Development];
	public downloadName = 'sublime_text_build_x64_setup.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'sublime-text.png';
	public homepage = 'https://sublimetext.com';

	public async resolveDownloadUrl() {
		const res = await fetch('https://www.sublimetext.com/download_thanks?target=win-x64');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/download\.sublimetext\.com\/sublime_text_build_\d+_x64_setup.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
