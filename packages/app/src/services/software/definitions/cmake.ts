import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'cmake';
	public name = 'CMake';
	public category = [SoftwareCategory.Development];
	public downloadName = 'cmake-windows-x86_64.msi';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'cmake.png';
	public homepage = 'https://cmake.org';

	public async resolveDownloadUrl() {
		const owner   = 'Kitware';
		const repo    = 'CMake';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('-windows-x86_64.msi'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
