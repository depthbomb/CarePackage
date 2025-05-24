import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'steam';
	public name = 'Steam';
	public category = [
		SoftwareCategory.Gaming,
		SoftwareCategory.Social,
	];
	public downloadName = 'SteamSetup.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = true;
	public deprecated = false;
	public icon = 'steam.png';
	public homepage = 'https://store.steampowered.com';

	public async resolveDownloadUrl() {
		return ok('https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe');
	}
}
