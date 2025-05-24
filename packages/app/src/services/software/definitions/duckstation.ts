import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'duckstation';
	public name = 'DuckStation';
	public category = [SoftwareCategory.Emulation, SoftwareCategory.Gaming];
	public downloadName = 'duckstation-windows-x64-release.zip';
	public isArchive = true;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'duckstation.png';
	public homepage = 'https://duckstation.org';

	public async resolveDownloadUrl() {
		const owner   = 'stenzek';
		const repo    = 'duckstation';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('duckstation-windows-x64-release.zip'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
