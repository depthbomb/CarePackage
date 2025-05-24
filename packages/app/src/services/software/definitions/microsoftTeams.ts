import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'microsoft-teams';
	public name = 'Microsoft Teams';
	public category = [SoftwareCategory.Social];
	public downloadName = 'MSTeamsSetup.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'microsoft-teams.png';
	public homepage = 'https://microsoft.com/en-us/microsoft-teams';

	public async resolveDownloadUrl() {
		return ok('https://go.microsoft.com/fwlink/?linkid=2281613&clcid=0x409&culture=en-us&country=us');
	}
}
