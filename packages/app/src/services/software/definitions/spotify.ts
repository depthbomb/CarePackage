import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'spotify';
	public name = 'Spotify';
	public category = [SoftwareCategory.Audio, SoftwareCategory.Media];
	public downloadName = 'SpotifySetup.exe';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'spotify.png';
	public homepage = 'https://spotify.com';

	public async resolveDownloadUrl() {
		return ok('https://download.scdn.co/SpotifySetup.exe');
	}
}
