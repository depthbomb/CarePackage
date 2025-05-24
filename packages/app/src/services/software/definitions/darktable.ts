import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'darktable';
	public name = 'darktable';
	public category = [SoftwareCategory.Creative, SoftwareCategory.Media];
	public downloadName = 'darktable-win64.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = true;
	public deprecated = false;
	public icon = 'darktable.png';
	public homepage = 'https://darktable.org';

	public async resolveDownloadUrl() {
		const owner   = 'darktable-org';
		const repo    = 'darktable';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('-win64.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
