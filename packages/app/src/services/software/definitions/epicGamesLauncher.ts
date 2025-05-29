import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'epic-games-launcher';
	public name = 'Epic Games Launcher';
	public category = [SoftwareCategory.Gaming];
	public downloadName = 'EpicGamesLauncherInstaller.msi';
	public icon = 'epic-games-launcher.png';
	public homepage = 'https://store.epicgames.com';

	public async resolveDownloadUrl() {
		return ok('https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi');
	}
}
