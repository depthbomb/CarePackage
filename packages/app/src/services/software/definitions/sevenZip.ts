import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'seven-zip';
	public name = '7-Zip';
	public category = [SoftwareCategory.FileManagement, SoftwareCategory.Utility];
	public downloadName = '7zSetup.msi';
	public shouldCacheUrl = true;
	public icon = '7zip.png';
	public homepage = 'https://7-zip.org';

	public async resolveDownloadUrl() {
		const owner   = 'ip7z';
		const repo    = '7zip';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('-x64.msi'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
