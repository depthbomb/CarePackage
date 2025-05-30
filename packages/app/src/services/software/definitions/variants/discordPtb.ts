import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'discord-ptb';
	public name = 'Discord PTB';
	public category = [SoftwareCategory.Social];
	public downloadName = 'DiscordPTBSetup.exe';
	public icon = 'discord.png';
	public homepage = 'https://ptb.discord.com';
	public parent = 'discord';

	public async resolveDownloadUrl() {
		return ok('https://ptb.discord.com/api/downloads/distributions/app/installers/latest?channel=ptb&platform=win&arch=x64');
	}
}
