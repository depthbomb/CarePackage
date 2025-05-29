import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'opera-gx';
	public name = 'Opera GX';
	public category = [SoftwareCategory.Browser];
	public downloadName = 'OperaGXSetup.exe';
	public icon = 'operagx.png';
	public homepage = 'https://opera.com/gx';

	public async resolveDownloadUrl() {
		return ok('https://net.geo.opera.com/opera_gx/stable/windows');
	}
}
