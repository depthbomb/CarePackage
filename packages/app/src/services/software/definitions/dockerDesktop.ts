import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'docker-desktop';
	public name = 'Docker Desktop';
	public category = [SoftwareCategory.Development];
	public downloadName = 'Docker Desktop Installer.exe';
	public icon = 'docker-desktop.png';
	public homepage = 'https://docker.com/products/docker-desktop';

	public async resolveDownloadUrl() {
		return ok('https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe');
	}
}
