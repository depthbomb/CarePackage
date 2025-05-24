import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'dolphin-emulator';
	public name = 'Dolphin Emulator';
	public category = [SoftwareCategory.Emulation, SoftwareCategory.Gaming];
	public downloadName = 'DolphinEmu.7z';
	public isArchive = true;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'dolphin-emu.png';
	public homepage = 'https://dolphin-emu.org';

	public async resolveDownloadUrl() {
		const res = await fetch('https://dolphin-emu.org/download/list/releases/1/');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/dl\.dolphin-emu\.org\/(?:releases\/\d+|builds\/[\da-f]{2}\/[\da-f]{2})\/dolphin-(?:\d+|master-\d+\.\d+-\d+)-x64\.7z/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
