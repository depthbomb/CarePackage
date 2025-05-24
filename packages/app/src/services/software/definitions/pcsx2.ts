import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'pcsx2-stable';
	public name = 'PCSX2';
	public category = [SoftwareCategory.Emulation, SoftwareCategory.Gaming];
	public downloadName = 'PCSX2.7z';
	public isArchive = true;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'pcsx2.png';
	public homepage = 'https://pcsx2.net';

	public async resolveDownloadUrl() {
		const owner   = 'pcsx2';
		const repo    = 'pcsx2';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('windows-x64-Qt.7z'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
