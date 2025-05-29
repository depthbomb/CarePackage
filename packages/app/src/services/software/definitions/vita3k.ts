import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'vita3k';
	public name = 'Vita3K';
	public category = [SoftwareCategory.Emulation, SoftwareCategory.Gaming];
	public downloadName = 'vita3k-windows-latest.zip';
	public isArchive = true;
	public icon = 'vita3k.png';
	public homepage = 'https://vita3k.org';

	public async resolveDownloadUrl() {
		return ok('https://github.com/Vita3K/Vita3K/releases/download/continuous/windows-latest.zip');
	}
}
