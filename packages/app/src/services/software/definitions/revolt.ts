import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'revolt';
	public name = 'Revolt';
	public category = [SoftwareCategory.Social];
	public downloadName = 'Revolt-Setup.exe';
	public shouldCacheUrl = true;
	public icon = 'revolt.png';
	public homepage = 'https://revolt.chat';

	public async resolveDownloadUrl() {
		const owner   = 'revoltchat';
		const repo    = 'desktop';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
