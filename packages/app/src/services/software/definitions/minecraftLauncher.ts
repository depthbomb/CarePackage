import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'minecraft-launcher';
	public name = 'Minecraft Launcher';
	public category = [SoftwareCategory.Gaming];
	public downloadName = '';
	public icon = 'minecraft-launcher.png';
	public homepage = 'https://minecraft.net';

	public async resolveDownloadUrl() {
		return ok('');
	}
}
