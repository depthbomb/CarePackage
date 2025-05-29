import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'peazip';
	public name = 'PeaZip';
	public category = [SoftwareCategory.FileManagement, SoftwareCategory.Utility];
	public downloadName = 'peazip.WIN64.exe';
	public shouldCacheUrl = true;
	public icon = 'peazip.png';
	public homepage = 'https://peazip.github.io';

	public async resolveDownloadUrl() {
		const owner   = 'peazip';
		const repo    = 'PeaZip';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('.WIN64.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
