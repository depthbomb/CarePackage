import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'git-for-windows';
	public name = 'Git for Windows';
	public category = [SoftwareCategory.Development, SoftwareCategory.FileManagement];
	public downloadName = 'Git-64-bit.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'git.png';
	public homepage = 'https://git-scm.com';

	public async resolveDownloadUrl() {
		const owner   = 'git-for-windows';
		const repo    = 'git';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.includes('Git-') && r.endsWith('-64-bit.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
