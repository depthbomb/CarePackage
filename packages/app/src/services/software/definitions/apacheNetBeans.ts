import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'apache-netbeans';
	public name = 'Apache NetBeans';
	public category = [SoftwareCategory.Development];
	public downloadName = 'Apache-NetBeans.exe';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = true;
	public deprecated = false;
	public icon = 'apache-netbeans.png';
	public homepage = 'https://netbeans.apache.org';

	public async resolveDownloadUrl() {
		const owner   = 'codelerity';
		const repo    = 'netbeans-installers';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
