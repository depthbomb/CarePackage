import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'visual-studio-community';
	public name = 'Visual Studio 2022 Community';
	public category = [SoftwareCategory.Development];
	public downloadName = 'VisualStudioSetup.exe';
	public shouldCacheUrl = true;
	public icon = 'visual-studio-community.png';
	public homepage = 'https://visualstudio.microsoft.com';

	public async resolveDownloadUrl() {
		const res = await fetch('https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&channel=Release');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/c2rsetup\.officeapps\.live\.com\/c2r\/downloadVS\.aspx\?sku=community&channel=Release&version=VS\d{4}&passive=true/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
