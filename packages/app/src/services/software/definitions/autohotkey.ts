import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'autohotkey';
	public name = 'AutoHotKey';
	public category = [SoftwareCategory.Utility];
	public downloadName = 'AutoHotkey_setup.exe';
	public shouldCacheUrl = true;
	public icon = 'autohotkey.png';
	public homepage = 'https://autohotkey.com';

	public async resolveDownloadUrl() {
		const owner   = 'AutoHotkey';
		const repo    = 'AutoHotkey';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('_setup.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
