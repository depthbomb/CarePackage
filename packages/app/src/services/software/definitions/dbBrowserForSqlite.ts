import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'db-browser-for-sqlite';
	public name = 'DB Browser for SQLite';
	public category = [SoftwareCategory.Development, SoftwareCategory.Utility];
	public downloadName = 'DB.Browser.for.SQLite-win64.msi';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'db-browser-for-sqlite.png';
	public homepage = 'https://sqlitebrowser.org';

	public async resolveDownloadUrl() {
		const owner   = 'sqlitebrowser';
		const repo    = 'sqlitebrowser';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('-win64.msi'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
