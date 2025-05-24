import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'megasync';
	public name = 'MEGAsync';
	public category = [SoftwareCategory.FileManagement, SoftwareCategory.Utility];
	public downloadName = 'MEGAsyncSetup64.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'megasync.png';
	public homepage = 'https://mega.io/desktop';

	public async resolveDownloadUrl() {
		return ok('https://mega.nz/MEGAsyncSetup64.exe');
	}
}
