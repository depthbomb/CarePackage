import { ok, err } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import { GithubReleasesScraper } from '../githubReleasesScraper';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'caesium-image-compressor';
	public name = 'Caesium Image Compressor';
	public category = [SoftwareCategory.Utility];
	public downloadName = 'caesium-image-compressor-win-setup.exe';
	public shouldCacheUrl = true;
	public icon = 'caesium-image-compressor.png';
	public homepage = 'https://saerasoft.com/caesium';

	public async resolveDownloadUrl() {
		const owner   = 'Lymphatus';
		const repo    = 'caesium-image-compressor';
		const release = await GithubReleasesScraper.getRelease(owner, repo, r => r.endsWith('.exe'));
		if (release.isErr()) {
			return err(release.error);
		}

		return ok(release.value);
	}
}
