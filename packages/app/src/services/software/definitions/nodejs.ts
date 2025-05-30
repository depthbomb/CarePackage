import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'nodejs';
	public name = 'Node.js';
	public category = [SoftwareCategory.Development, SoftwareCategory.Runtime];
	public downloadName = '';
	public icon = 'nodejs.png';
	public homepage = 'https://nodejs.org';

	public async resolveDownloadUrl() {
		return ok('');
	}
}
