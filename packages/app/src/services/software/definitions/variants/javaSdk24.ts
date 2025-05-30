import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'java-sdk-24';
	public name = 'Java SE Development Kit 24.x';
	public category = [SoftwareCategory.Development, SoftwareCategory.Runtime];
	public downloadName = 'jdk-24_windows-x64_bin.msi';
	public icon = 'java.png';
	public homepage = 'https://oracle.com/java/technologies/downloads';
	public parent = 'java-sdk';

	public async resolveDownloadUrl() {
		return ok('https://download.oracle.com/java/24/latest/jdk-24_windows-x64_bin.msi');
	}
}
