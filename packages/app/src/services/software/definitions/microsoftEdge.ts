import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'microsoft-edge';
	public name = 'Microsoft Edge';
	public category = [SoftwareCategory.Browser];
	public downloadName = 'MicrosoftEdgeSetup.exe';
	public icon = 'microsoft-edge.png';
	public homepage = 'https://microsoft.com/en-us/edge';

	public async resolveDownloadUrl() {
		return ok('https://c2rsetup.officeapps.live.com/c2r/downloadEdge.aspx?platform=Default&source=EdgeStablePage&Channel=Stable&language=en&brand=M100');
	}
}
