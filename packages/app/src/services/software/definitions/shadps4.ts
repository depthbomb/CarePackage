import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'shadps4';
	public name = 'shadPS4';
	public category = [SoftwareCategory.Emulation, SoftwareCategory.Gaming];
	public downloadName = 'shadps4-win64-qt.zip';
	public isArchive = true;
	public shouldCacheUrl = true;
	public icon = 'shadps4.png';
	public homepage = 'https://shadps4.net';

	public async resolveDownloadUrl() {
		const owner   = 'shadps4-emu';
		const repo    = 'shadPS4';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.includes('shadps4-win64-qt'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
