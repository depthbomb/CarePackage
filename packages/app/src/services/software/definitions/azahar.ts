import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'azahar';
	public name = 'Azahar';
	public category = [SoftwareCategory.Emulation, SoftwareCategory.Gaming];
	public downloadName = 'azahar-windows-msys2-installer.exe';
	public shouldCacheUrl = true;
	public icon = 'azahar.png';
	public homepage = 'https://azahar-emu.org';

	public async resolveDownloadUrl() {
		const owner   = 'azahar-emu';
		const repo    = 'azahar';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('-windows-msys2-installer.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
