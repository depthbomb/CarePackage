import { ok } from 'neverthrow';
import { randomUUID } from 'node:crypto';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'adobe-creative-cloud';
	public name = 'Adobe Creative Cloud';
	public category = [SoftwareCategory.Creative];
	public downloadName = 'Creative_Cloud_Set-Up.exe';
	public icon = 'adobe-creative-cloud.png';
	public homepage = 'https://www.adobe.com/creativecloud.html';

	public async resolveDownloadUrl() {
		return ok(`https://prod-rel-ffc-ccm.oobesaas.adobe.com/adobe-ffc-external/core/v1/wam/download?sapCode=KCCC&productName=Creative%20Cloud&os=win&guid=${randomUUID()}&environment=prod&api_key=CCHomeWeb1`);
	}
}
