import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'playstation-accessories';
	public name = 'PlayStation Accessories';
	public category = [SoftwareCategory.Gaming, SoftwareCategory.Peripheral];
	public downloadName = 'PlayStationAccessoriesInstaller.exe';
	public requiresAdmin = true;
	public icon = 'playstation-accessories.png';
	public homepage = 'https://controller.dl.playstation.net/controller/lang/en/2100004.html';

	public async resolveDownloadUrl() {
		return ok('https://fwupdater.dl.playstation.net/fwupdater/PlayStationAccessoriesInstaller.exe');
	}
}
