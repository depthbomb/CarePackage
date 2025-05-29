import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'evernote';
	public name = 'Evernote';
	public category = [SoftwareCategory.Productivity];
	public downloadName = 'Evernote-latest.exe';
	public icon = 'evernote.png';
	public homepage = 'https://evernote.com';

	public async resolveDownloadUrl() {
		return ok('https://win.desktop.evernote.com/builds/Evernote-latest.exe');
	}
}
