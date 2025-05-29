import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'heroic-games-launcher';
	public name = 'Heroic Games Launcher';
	public category = [SoftwareCategory.Gaming];
	public downloadName = 'Heroic-Setup-x64.exe';
	public shouldCacheUrl = true;
	public icon = 'heroic-games-launcher.png';
	public homepage = 'https://heroicgameslauncher.com';

	public async resolveDownloadUrl() {
		const owner   = 'Heroic-Games-Launcher';
		const repo    = 'HeroicGamesLauncher';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('-Setup-x64.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
