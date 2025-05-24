import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'discord-stable';
	public name = 'Discord';
	public category = [SoftwareCategory.Social];
	public downloadName = 'DiscordSetup.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'discord.png';
	public homepage = 'https://discord.com';

	public async resolveDownloadUrl() {
		return ok('https://discord.com/api/downloads/distributions/app/installers/latest?channel=stable&platform=win&arch=x64');
	}
}
