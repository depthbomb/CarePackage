import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'github-desktop';
	public name = 'GitHub Desktop';
	public category = [SoftwareCategory.Development];
	public downloadName = 'GitHubDesktopSetup-x64.exe';
	public icon = 'github-desktop.png';
	public homepage = 'https://desktop.github.com';

	public async resolveDownloadUrl() {
		return ok('https://central.github.com/deployments/desktop/desktop/latest/win32');
	}
}
