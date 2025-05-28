import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'microsoft-onedrive';
	public name = 'Microsoft OneDrive';
	public category = [SoftwareCategory.FileManagement, SoftwareCategory.Utility];
	public downloadName = 'OneDriveSetup.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'microsoft-onedrive.png';
	public homepage = 'https://microsoft.com/en-us/microsoft-365/onedrive';

	public async resolveDownloadUrl() {
		return ok('https://go.microsoft.com/fwlink/?linkid=844652');
	}
}
