import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'rufus';
	public name = 'Rufus';
	public category = [SoftwareCategory.FileManagement, SoftwareCategory.Utility];
	public downloadName = 'rufus.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = true;
	public deprecated = false;
	public icon = 'rufus.png';
	public homepage = 'https://rufus.ie';

	public async resolveDownloadUrl() {
		const owner   = 'pbatard';
		const repo    = 'rufus';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => !!r.match(/rufus-\d+\.\d+\.exe/));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
