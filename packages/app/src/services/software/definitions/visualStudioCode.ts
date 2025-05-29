import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'visual-studio-code';
	public name = 'Visual Studio Code';
	public category = [SoftwareCategory.Development];
	public downloadName = 'VSCodeUserSetup-x64.exe';
	public icon = 'visual-studio-code.png';
	public homepage = 'https://code.visualstudio.com';

	public async resolveDownloadUrl() {
		return ok('https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user');
	}
}
