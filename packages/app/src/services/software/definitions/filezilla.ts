import { ok, err } from 'neverthrow';
import { BROWSER_USER_AGENT } from '~/constants';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'filezilla';
	public name = 'FileZilla';
	public category = [SoftwareCategory.Development, SoftwareCategory.FileManagement, SoftwareCategory.Network];
	public downloadName = 'FileZilla_win64-setup.exe';
	public icon = 'filezilla.png';
	public homepage = 'https://filezilla-project.org';

	public async resolveDownloadUrl() {
		const res = await fetch('https://filezilla-project.org/download.php?show_all=1', {
			headers: {
				'user-agent': BROWSER_USER_AGENT,
				'accept': '*/*',
				'referer': 'https://filezilla-project.org'
			}
		});
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/dl\d+\.cdn\.filezilla-project\.org\/client\/FileZilla_\d+\.\d+\.\d+_win64-setup\.exe\?h=[a-zA-Z0-9-_]{22,}&x=\d{10,}/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
