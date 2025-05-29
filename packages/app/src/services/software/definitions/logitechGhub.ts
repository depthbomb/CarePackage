import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'logitech-g-hub';
	public name = 'Logitech G HUB';
	public category = [SoftwareCategory.Peripheral];
	public downloadName = 'lghub_installer.exe';
	public requiresAdmin = true;
	public icon = 'logitech-g-hub.png';
	public homepage = 'https://logitechg.com/en-us/innovation/g-hub.html';

	public async resolveDownloadUrl() {
		return ok('https://download01.logi.com/web/ftp/pub/techsupport/gaming/lghub_installer.exe');
	}
}
