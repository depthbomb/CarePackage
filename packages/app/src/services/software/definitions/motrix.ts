import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'motrix';
	public name = 'Motrix';
	public category = [SoftwareCategory.FileManagement, SoftwareCategory.Utility];
	public downloadName = 'Motrix-x64.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'motrix.png';
	public homepage = 'https://motrix.app';

	public async resolveDownloadUrl() {
		const owner   = 'agalwood';
		const repo    = 'Motrix';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('-x64.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
