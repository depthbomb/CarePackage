import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'minecraft-launcher-legacy';
	public name = 'Minecraft Launcher (Legacy)';
	public category = [SoftwareCategory.Gaming];
	public downloadName = 'MinecraftInstaller.msi';
	public icon = 'minecraft-launcher-legacy.png';
	public homepage = 'https://minecraft.net';

	public async resolveDownloadUrl() {
		return ok('https://launcher.mojang.com/download/MinecraftInstaller.msi?ref=mcnet');
	}
}
