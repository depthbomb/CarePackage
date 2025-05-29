import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'powershell-core';
	public name = 'PowerShell 7';
	public category = [SoftwareCategory.Development, SoftwareCategory.Utility];
	public downloadName = 'powershell-win-x64.msi';
	public shouldCacheUrl = true;
	public icon = 'powershell-core.png';
	public homepage = 'https://github.com/PowerShell/PowerShell';

	public async resolveDownloadUrl() {
		const owner   = 'PowerShell';
		const repo    = 'PowerShell';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('-win-x64.msi'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
