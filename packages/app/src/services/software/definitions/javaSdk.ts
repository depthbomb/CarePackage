import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'java-sdk';
	public name = 'Java SE Development Kit';
	public category = [SoftwareCategory.Development, SoftwareCategory.Runtime];
	public downloadName = '';
	public icon = 'java.png';
	public homepage = 'https://oracle.com/java/technologies/downloads';

	public async resolveDownloadUrl() {
		return ok('');
	}
}
