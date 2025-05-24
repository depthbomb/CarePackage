import { ok, err } from 'neverthrow';
import { DownloadUrlResolveError } from 'shared';

export class GithubReleasesScraper {
	public static async getRelease(owner: string, repo: string, predicate: (releases: string) => boolean) {
		const initialRes = await fetch(`https://github.com/${owner}/${repo}/releases/latest`, { redirect: 'follow' });
		if (initialRes.status >= 400) {
			return err(DownloadUrlResolveError.GitHubRequestError);
		}

		const tag = initialRes.url.split('/').pop();

		let assetsRes = await fetch(`https://github.com/${owner}/${repo}/releases/expanded_assets/${tag}`);
		if (assetsRes.status === 404) {
			assetsRes = await fetch(`https://github.com/${owner}/${repo}/releases/expanded_assets/release/${tag}`);
		}

		if (!assetsRes.ok) {
			return err(DownloadUrlResolveError.GitHubRequestError);
		}

		const html    = await assetsRes.text();
		const matches = html.matchAll(/href="(.*)" rel="nofollow"/g);
		const assets  = [...matches].map(m => `https://github.com${m[1]}`);
		const asset   = assets.find(predicate);
		if (!asset) {
			return err(DownloadUrlResolveError.GitHubAssetNotFoundError);
		}

		return ok(asset);
	}
}
