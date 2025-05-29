import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'unity-hub';
	public name = 'Unity Hub';
	public category = [SoftwareCategory.Creative, SoftwareCategory.GameDevelopment];
	public downloadName = 'UnityHubSetup.exe';
	public requiresAdmin = true;
	public icon = 'unity-hub.png';
	public homepage = 'https://unity.com';

	public async resolveDownloadUrl() {
		return ok('https://public-cdn.cloud.unity3d.com/hub/prod/UnityHubSetup.exe');
	}
}
