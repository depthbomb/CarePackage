import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'nvidia-app';
	public name = 'NVIDIA App';
	public category = [SoftwareCategory.Peripheral];
	public downloadName = 'NVIDIA_app.exe';
	public shouldCacheUrl = true;
	public requiresAdmin = true;
	public icon = 'nvidia.png';
	public homepage = 'https://nvidia.com/en-us/software/nvidia-app';

	public async resolveDownloadUrl() {
		const res = await fetch('https://nvidia.com/en-us/software/nvidia-app');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/us.download.nvidia.com\/nvapp\/client\/.*\/NVIDIA_app_.*\.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
