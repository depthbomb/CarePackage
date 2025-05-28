import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'ccleaner';
	public name = 'CCleaner';
	public category = [SoftwareCategory.FileManagement, SoftwareCategory.SystemManagement, SoftwareCategory.Utility];
	public downloadName = 'ccsetup.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = true;
	public deprecated = false;
	public icon = 'ccleaner.png';
	public homepage = 'https://ccleaner.com';

	public async resolveDownloadUrl() {
		return ok('https://bits.avcdn.net/productfamily_CCLEANER/insttype_FREE/platform_WIN_PIR/installertype_ONLINE/build_RELEASE');
	}
}
