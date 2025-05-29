import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

type Response = {
	result: {
		downloadVO: {
			zoomX64: {
				version: string;
				packageName: string;
				archType: string;
			}
		};
	};
};

export default class implements ISoftwareDefinition {
	public key = 'zoom-workplace';
	public name = 'Zoom Workplace';
	public category = [SoftwareCategory.Social];
	public downloadName = 'ZoomInstallerFull.exe';
	public shouldCacheUrl = true;
	public icon = 'zoom.png';
	public homepage = 'https://zoom.us';

	public async resolveDownloadUrl() {
		const res = await fetch('https://zoom.us/rest/download?os=win');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const json                               = await res.json() as Response;
		const { version, packageName, archType } = json.result.downloadVO.zoomX64;

		return ok(`https://zoom.us/client/${version}/${packageName}?archType=${archType}`);
	}
}
