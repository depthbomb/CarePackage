import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'paint-dot-net';
	public name = 'Paint.NET';
	public category = [SoftwareCategory.Creative];
	public downloadName = 'Paint.NET.zip';
	public isArchive = true;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'paintdotnet.png';
	public homepage = 'https://getpaint.net';

	public async resolveDownloadUrl() {
		const owner   = 'paintdotnet';
		const repo    = 'release';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('.install.x64.zip'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
