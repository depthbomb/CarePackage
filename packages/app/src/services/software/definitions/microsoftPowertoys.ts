import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'microsoft-powertoys';
	public name = 'Microsoft PowerToys (Preview)';
	public category = [SoftwareCategory.Utility];
	public downloadName = 'PowerToysUserSetup-x64.exe';
	public shouldCacheUrl = true;
	public icon = 'powertoys.png';
	public homepage = 'https://learn.microsoft.com/en-us/windows/powertoys';

	public async resolveDownloadUrl() {
		const owner   = 'microsoft';
		const repo    = 'PowerToys';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.includes('PowerToysSetup-') && r.endsWith('-x64.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
