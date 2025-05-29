import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'melonds';
	public name = 'melonDS';
	public category = [SoftwareCategory.Emulation, SoftwareCategory.Gaming];
	public downloadName = 'melonDS-windows-x86_64.zip';
	public isArchive = true;
	public icon = 'melonds.png';
	public homepage = 'https://melonds.kuribo64.net';

	public async resolveDownloadUrl() {
		return ok('https://melonds.kuribo64.net/downloads/melonDS-windows-x86_64.zip');
	}
}
