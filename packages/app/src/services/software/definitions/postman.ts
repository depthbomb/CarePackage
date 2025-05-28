import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'postman';
	public name = 'Postman';
	public category = [SoftwareCategory.Development, SoftwareCategory.Network];
	public downloadName = 'Postman-win64-Setup.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'postman.png';
	public homepage = 'https://postman.com';

	public async resolveDownloadUrl() {
		return ok('https://dl.pstmn.io/download/latest/win64');
	}
}
