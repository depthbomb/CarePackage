import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'godot';
	public name = 'Godot';
	public category = [SoftwareCategory.Creative, SoftwareCategory.GameDevelopment];
	public downloadName = '';
	public icon = 'godot.png';
	public homepage = 'https://godotengine.org';

	public async resolveDownloadUrl() {
		return ok('');
	}
}
