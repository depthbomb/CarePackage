import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'godot';
	public name = 'Godot';
	public category = [
		SoftwareCategory.Creative,
		SoftwareCategory.GameDevelopment,
	];
	public downloadName = 'Godot-stable_win64.exe.zip';
	public isArchive = true;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'godot.png';
	public homepage = 'https://godotengine.org';

	public async resolveDownloadUrl() {
		const owner   = 'godotengine';
		const repo    = 'godot';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('-stable_win64.exe.zip'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
