import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'slack';
	public name = 'Slack';
	public category = [SoftwareCategory.Social];
	public downloadName = 'SlackSetup.exe';
	public icon = 'slack.png';
	public homepage = 'https://slack.com';

	public async resolveDownloadUrl() {
		return ok('https://slack.com/api/desktop.latestRelease?arch=x64&variant=exe&redirect=true');
	}
}
