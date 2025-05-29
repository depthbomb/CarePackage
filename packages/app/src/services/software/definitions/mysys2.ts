import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'msys2';
	public name = 'MSYS2';
	public category = [SoftwareCategory.Development];
	public downloadName = 'msys-x86_64.exe';
	public shouldCacheUrl = true;
	public icon = 'msys2.png';
	public homepage = 'https://msys2.org';

	public async resolveDownloadUrl() {
		const owner   = 'msys2';
		const repo    = 'msys2-installer';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.includes('msys2-x86_64-') && r.endsWith('.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
