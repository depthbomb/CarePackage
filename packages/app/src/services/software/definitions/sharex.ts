import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'sharex';
	public name = 'ShareX';
	public category = [SoftwareCategory.Media, SoftwareCategory.Utility];
	public downloadName = 'ShareX-setup.exe';
	public shouldCacheUrl = true;
	public icon = 'sharex.png';
	public homepage = 'https://getsharex.com';

	public async resolveDownloadUrl() {
		const owner   = 'ShareX';
		const repo    = 'ShareX';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('-setup.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
