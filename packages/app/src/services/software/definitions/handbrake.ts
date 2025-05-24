import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'handbrake';
	public name = 'HandBrake';
	public category = [
		SoftwareCategory.Media,
		SoftwareCategory.Utility,
	];
	public downloadName = 'HandBrake-x86_64-Win_GUI.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = true;
	public deprecated = false;
	public icon = 'handbrake.png';
	public homepage = 'https://handbrake.fr';

	public async resolveDownloadUrl() {
		const owner   = 'HandBrake';
		const repo    = 'HandBrake';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('-x86_64-Win_GUI.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
