import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'dotnet';
	public name = '.NET';
	public category = [SoftwareCategory.Development, SoftwareCategory.Runtime];
	public downloadName = '';
	public icon = 'dotnet.png';
	public homepage = 'https://dot.net';

	public async resolveDownloadUrl() {
		return ok('');
	}
}
