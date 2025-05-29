import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'teracopy';
	public name = 'TeraCopy';
	public category = [SoftwareCategory.FileManagement, SoftwareCategory.Utility];
	public downloadName = 'teracopy.exe';
	public icon = 'teracopy.png';
	public homepage = 'https://codesector.com/teracopy';

	public async resolveDownloadUrl() {
		return ok('https://codesector.com/files/teracopy.exe');
	}
}
