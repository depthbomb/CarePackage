import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'rainmeter';
	public name = 'Rainmeter';
	public category = [SoftwareCategory.Utility];
	public downloadName = 'Rainmeter.exe';
	public shouldCacheUrl = true;
	public icon = 'rainmeter.png';
	public homepage = 'https://rainmeter.net';

	public async resolveDownloadUrl() {
		const owner   = 'rainmeter';
		const repo    = 'rainmeter';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
