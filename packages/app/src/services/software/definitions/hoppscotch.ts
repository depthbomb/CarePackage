import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'hoppscotch-desktop';
	public name = 'Hoppscotch';
	public category = [SoftwareCategory.Development, SoftwareCategory.Network];
	public downloadName = 'Hoppscotch_win_x64.msi';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'hoppscotch.png';
	public homepage = 'https://hoppscotch.io';

	public async resolveDownloadUrl() {
		const owner   = 'hoppscotch';
		const repo    = 'releases';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('Hoppscotch_win_x64.msi'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
