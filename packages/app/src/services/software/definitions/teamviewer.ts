import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'teamviewer';
	public name = 'TeamViewer';
	public category = [SoftwareCategory.Social, SoftwareCategory.Utility];
	public downloadName = 'TeamViewer_Setup_x64.exe';
	public icon = 'teamviewer.png';
	public homepage = 'https://teamviewer.com';

	public async resolveDownloadUrl() {
		return ok('https://download.teamviewer.com/download/TeamViewer_Setup_x64.exe');
	}
}
