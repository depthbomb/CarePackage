import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'godot-cs';
	public name = 'Godot (C# support)';
	public category = [SoftwareCategory.Creative, SoftwareCategory.GameDevelopment];
	public downloadName = 'Godot-stable_mono_win64.zip';
	public isArchive = true;
	public shouldCacheUrl = true;
	public icon = 'godot.png';
	public homepage = 'https://godotengine.org';
	public parent = 'godot';

	public async resolveDownloadUrl() {
		const owner   = 'godotengine';
		const repo    = 'godot';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('-stable_mono_win64.zip'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
