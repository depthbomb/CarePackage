import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'dnspy-ex';
	public name = 'dnSpy (Fork)';
	public category = [SoftwareCategory.Development, SoftwareCategory.Utility];
	public downloadName = 'dnSpy-net-win64.zip';
	public isArchive = true;
	public shouldCacheUrl = true;
	public icon = 'dnspy.png';
	public homepage = 'https://github.com/dnSpyEx/dnSpy';

	public async resolveDownloadUrl() {
		const owner   = 'dnSpyEx';
		const repo    = 'dnSpy';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('win64.zip'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
