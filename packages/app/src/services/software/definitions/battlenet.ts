import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'blizzard-battle-net';
	public name = 'Battle.net';
	public category = [SoftwareCategory.Gaming];
	public downloadName = 'Battle.net-Setup.exe';
	public icon = 'battlenet.png';
	public homepage = 'https://battle.net';

	public async resolveDownloadUrl() {
		return ok('https://downloader.battle.net/download/getInstallerForGame?os=win&gameProgram=BATTLENET_APP&version=Live');
	}
}
