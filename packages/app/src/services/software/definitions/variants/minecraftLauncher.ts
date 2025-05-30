import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'minecraft-launcher-latest';
	public name = 'Minecraft Launcher';
	public category = [SoftwareCategory.Gaming];
	public downloadName = 'MinecraftInstaller.exe';
	public icon = 'minecraft-launcher.png';
	public homepage = 'https://minecraft.net';
	public parent = 'minecraft-launcher';

	public async resolveDownloadUrl() {
		return ok('https://launcher.mojang.com/download/MinecraftInstaller.exe?ref=mcnet');
	}
}
