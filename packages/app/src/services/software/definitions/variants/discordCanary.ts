import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'discord-canary';
	public name = 'Discord Canary';
	public category = [SoftwareCategory.Social];
	public downloadName = 'DiscordCanarySetup.exe';
	public icon = 'discord-canary.png';
	public homepage = 'https://canary.discord.com';
	public parent = 'discord';

	public async resolveDownloadUrl() {
		return ok('https://canary.discord.com/api/downloads/distributions/app/installers/latest?channel=canary&platform=win&arch=x64');
	}
}
