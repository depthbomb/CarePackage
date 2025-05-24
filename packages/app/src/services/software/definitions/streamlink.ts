import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'streamlink';
	public name = 'Streamlink';
	public category = [SoftwareCategory.Media];
	public downloadName = 'streamlink-x86_64.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = true;
	public deprecated = false;
	public icon = 'streamlink.png';
	public homepage = 'https://streamlink.github.io';

	public async resolveDownloadUrl() {
		const owner   = 'streamlink';
		const repo    = 'windows-builds';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.match(/streamlink-\d+\.\d+\.\d+(?:-\d+)?-py3\d+-x86_64\.exe/) !== null);
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
