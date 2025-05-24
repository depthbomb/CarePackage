import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'notepad-plus-plus';
	public name = 'Notepad++';
	public category = [SoftwareCategory.Development];
	public downloadName = 'npp.Installer.x64.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = true;
	public deprecated = false;
	public icon = 'notepad-plus-plus.png';
	public homepage = 'https://notepad-plus-plus.org';

	public async resolveDownloadUrl() {
		const owner   = 'notepad-plus-plus';
		const repo    = 'notepad-plus-plus';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('.Installer.x64.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
