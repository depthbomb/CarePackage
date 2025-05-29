import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'glasswire';
	public name = 'GlassWire';
	public category = [SoftwareCategory.Network, SoftwareCategory.Utility];
	public downloadName = 'GlassWireSetup.exe';
	public requiresAdmin = true;
	public icon = 'glasswire.png';
	public homepage = 'https://glasswire.com';

	public async resolveDownloadUrl() {
		return ok('https://download.glasswire.com/GlassWireSetup.exe');
	}
}
