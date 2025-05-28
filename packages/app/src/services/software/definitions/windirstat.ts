import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'windirstat';
	public name = 'WinDirStat';
	public category = [SoftwareCategory.FileManagement, SoftwareCategory.SystemManagement, SoftwareCategory.Utility];
	public downloadName = 'WinDirStat-x64.msi';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'windirstat.png';
	public homepage = 'https://windirstat.net';

	public async resolveDownloadUrl() {
		const owner   = 'windirstat';
		const repo    = 'windirstat';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('-x64.msi'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
