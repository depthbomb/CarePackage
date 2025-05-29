import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'display-driver-uninstaller';
	public name = 'Display Driver Uninstaller';
	public category = [SoftwareCategory.Utility];
	public downloadName = '[Guru3D.com]-DDU.zip';
	public isArchive = true;
	public icon = 'ddu.png';
	public homepage = 'https://guru3d.com/download/display-driver-uninstaller-download';

	public async resolveDownloadUrl() {
		return ok('https://download-eu2.guru3d.com/ddu/[Guru3D]-DDU.zip');
	}
}
