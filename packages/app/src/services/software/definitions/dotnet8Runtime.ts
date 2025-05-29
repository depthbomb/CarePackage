import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'dotnet-8-runtime';
	public name = '.NET 8.0 Runtime';
	public category = [SoftwareCategory.DotNet];
	public downloadName = 'dotnet-runtime-8.0-win-x64.exe';
	public shouldCacheUrl = true;
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
		const match = html.match(/https:\/\/builds.dotnet.microsoft.com\/dotnet\/Runtime\/\d+\.\d+\.\d+\/dotnet-runtime-\d+\.\d+\.\d+-win-x64.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}

	private async getDownloadPageUrl() {
		const res = await fetch('https://dotnet.microsoft.com/en-us/download/dotnet/8.0');
		if (!res.ok) {
			return null;
		}

		const html  = await res.text();
		const match = html.match(/runtime-\d+\.\d+\.\d+-windows-x64-installer/);
		if (!match) {
			return null;
		}

		return `https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/${match[0]}`;
	}
}
