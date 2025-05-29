import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'obsidian';
	public name = 'Obsidian';
	public category = [SoftwareCategory.Productivity];
	public downloadName = 'Obsidian.exe';
	public shouldCacheUrl = true;
	public icon = 'obsidian.png';
	public homepage = 'https://obsidian.md';

	public async resolveDownloadUrl() {
		const owner   = 'obsidianmd';
		const repo    = 'obsidian-releases';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
