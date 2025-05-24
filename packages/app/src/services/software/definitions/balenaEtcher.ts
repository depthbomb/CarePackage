import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'balenaetcher';
	public name = 'balenaEtcher';
	public category = [SoftwareCategory.Utility];
	public downloadName = 'balenaEtcher.Setup.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'balenaetcher.png';
	public homepage = 'https://etcher.io';

	public async resolveDownloadUrl() {
		const owner   = 'balena-io';
		const repo    = 'etcher';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('.Setup.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
