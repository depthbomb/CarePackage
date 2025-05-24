import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'dotnet-9-desktop-runtime';
	public name = '.NET 9.0 Desktop Runtime';
	public category = [SoftwareCategory.DotNet];
	public downloadName = 'windowsdesktop-runtime-9.0-win-x64.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'dotnet.png';
	public homepage = 'https://dot.net';

	public async resolveDownloadUrl() {
		const downloadPageUrl = await this.getDownloadPageUrl();
		if (!downloadPageUrl) {
			return err(DownloadUrlResolveError.Generic);
		}

		const res = await fetch(downloadPageUrl);
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/builds.dotnet.microsoft.com\/dotnet\/WindowsDesktop\/\d+\.\d+\.\d+\/windowsdesktop-runtime-\d+\.\d+\.\d+-win-x64.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}

	private async getDownloadPageUrl() {
		const res = await fetch('https://dotnet.microsoft.com/en-us/download/dotnet/9.0');
		if (!res.ok) {
			return null;
		}

		const html  = await res.text();
		const match = html.match(/runtime-desktop-\d+\.\d+\.\d+-windows-x64-installer/);
		if (!match) {
			return null;
		}

		return `https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/${match[0]}`;
	}
}
