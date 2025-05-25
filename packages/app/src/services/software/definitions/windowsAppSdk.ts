import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'windows-app-sdk';
	public name = 'Windows App SDK';
	public category = [SoftwareCategory.Development, SoftwareCategory.Runtime];
	public downloadName = 'WindowsAppRuntimeInstall-x64.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'generic.png';
	public homepage = 'https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk';

	public async resolveDownloadUrl() {
		const res = await fetch('https://learn.microsoft.com/en-us/windows/apps/windows-app-sdk/downloads');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/aka.ms\/windowsappsdk\/\d+.\d+\/latest\/windowsappruntimeinstall-x64.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
