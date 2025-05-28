import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'qbittorrent';
	public name = 'qBittorrent';
	public category = [SoftwareCategory.FileManagement, SoftwareCategory.Network, SoftwareCategory.Utility];
	public downloadName = 'qbittorrent_x64_setup.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'qbittorrent.png';
	public homepage = 'https://qbittorrent.org';

	public async resolveDownloadUrl() {
		const payload = await this.getDownloadUrlPayload();
		if (!payload) {
			return err(DownloadUrlResolveError.Generic);
		}

		const res = await fetch('https://api.fosshub.com/download/', {
			method: 'POST',
			headers: {
				'content-type': 'application/json'
			},
			body: payload
		});
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const json = await res.json() as { data: { url: string; }; };

		return ok(json.data.url);
	}

	private async getDownloadUrlPayload() {
		const res = await fetch('https://www.fosshub.com/qBittorrent.html');
		if (!res.ok) {
			return null;
		}

		const text  = await res.text();
		const match = text.match(/<script>\s+var\s+settings\s+=(.*)\s+<\/script>/m);
		if (!match) {
			return null;
		}

		const json         = JSON.parse(match[1]);
		const projectId    = json.projectId as string;
		const projectUri   = json.pool.u as string;
		const projectFiles = json.pool.f as Array<{ n: string; r: string; }>;
		const latestFile   = projectFiles[0];

		return JSON.stringify({
			projectId,
			releaseId: latestFile.r,
			projectUri,
			fileName: latestFile.n,
			source: 'CF'
		});
	}
}
