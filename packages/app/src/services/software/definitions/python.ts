import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'python';
	public name = 'Python';
	public category = [SoftwareCategory.Development];
	public downloadName = '';
	public icon = 'python.png';
	public homepage = 'https://python.org';

	public async resolveDownloadUrl() {
		return ok('');
	}
}
