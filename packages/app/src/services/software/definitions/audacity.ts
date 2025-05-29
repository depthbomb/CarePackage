import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'audacity';
	public name = 'Audacity';
	public category = [SoftwareCategory.Audio, SoftwareCategory.Media];
	public downloadName = 'audacity-win-64bit.exe';
	public shouldCacheUrl = true;
	public icon = 'audacity.png';
	public homepage = 'https://audacityteam.org';

	public async resolveDownloadUrl() {
		const owner   = 'audacity';
		const repo    = 'audacity';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('-64bit.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
