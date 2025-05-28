import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'blender';
	public name = 'Blender';
	public category = [SoftwareCategory.Creative, SoftwareCategory.Modelling];
	public downloadName = 'blender-windows-x64.msi';
	public isArchive = false;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'blender.png';
	public homepage = 'https://blender.org';

	public async resolveDownloadUrl() {
		const res = await fetch('https://blender.org/download');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/www\.blender\.org\/download\/release\/(Blender\d+\.\d+\/blender-\d\.\d+.\d+-windows-x64\.msi)/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(`https://mirrors.iu13.net/blender/release/${match[1]}`);
	}
}
