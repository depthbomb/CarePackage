import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'jackett';
	public name = 'Jackett';
	public category = [SoftwareCategory.FileManagement, SoftwareCategory.Utility];
	public downloadName = 'Jackett.Installer.Windows.exe';
	public shouldCacheUrl = true;
	public icon = 'jackett.png';
	public homepage = 'https://github.com/Jackett/Jackett';

	public async resolveDownloadUrl() {
		const owner   = 'Jackett';
		const repo    = 'Jackett';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('Jackett.Installer.Windows.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
