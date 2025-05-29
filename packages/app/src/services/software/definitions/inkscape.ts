import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'inkscape';
	public name = 'Inkscape';
	public category = [SoftwareCategory.Creative];
	public downloadName = 'inkscape-x64.exe';
	public shouldCacheUrl = true;
	public requiresAdmin = true;
	public icon = 'inkscape.png';
	public homepage = 'https://inkscape.org';

	public async resolveDownloadUrl() {
		const redirectUrl = await this.getRedirectUrl();
		if (!redirectUrl) {
			return err(DownloadUrlResolveError.Generic);
		}

		const res = await fetch(`${redirectUrl}windows/64-bit/exe/dl`);
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/"(\/gallery\/item\/\d{5,}\/inkscape-.*-x64\.exe)"/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(`https://inkscape.org${match[1]}`);
	}

	private async getRedirectUrl() {
		const res = await fetch('https://inkscape.org/release');
		if (!res.ok) {
			return null;
		}

		return res.url;
	}
}
