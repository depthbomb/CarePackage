import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'cemu';
	public name = 'Cemu';
	public category = [SoftwareCategory.Emulation, SoftwareCategory.Gaming];
	public downloadName = 'cemu-windows-x64.zip';
	public isArchive = true;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'cemu.png';
	public homepage = 'https://cemu.info';

	public async resolveDownloadUrl() {
		const owner        = 'cemu-project';
		const repo         = 'Cemu';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('-windows-x64.zip'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
