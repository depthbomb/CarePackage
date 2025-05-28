import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'google-drive';
	public name = 'Google Drive';
	public category = [SoftwareCategory.FileManagement, SoftwareCategory.Utility];
	public downloadName = 'GoogleDriveSetup.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = true;
	public deprecated = false;
	public icon = 'google-drive.png';
	public homepage = 'https://workspace.google.com/products/drive';

	public async resolveDownloadUrl() {
		return ok('https://dl.google.com/drive-file-stream/GoogleDriveSetup.exe');
	}
}
