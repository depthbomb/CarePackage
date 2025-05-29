import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'trillian';
	public name = 'Trillian';
	public category = [SoftwareCategory.Social];
	public downloadName = 'trillian.exe';
	public shouldCacheUrl = true;
	public icon = 'trillian.png';
	public homepage = 'https://trillian.im';

	public async resolveDownloadUrl() {
		const res = await fetch('https://trillian.im/get/windows/thanks');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/<a href="(\/get\/windows\/.*\/)">Try downloading again\.<\/a>/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(`${this.homepage}${match[1]}`);
	}
}
