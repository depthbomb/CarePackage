import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'java-sdk-21';
	public name = 'Java SE Development Kit 21.x';
	public category = [
		SoftwareCategory.Development,
		SoftwareCategory.Runtime,
	];
	public downloadName = 'jdk-21_windows-x64_bin.msi';
	public isArchive = false;
	public shouldCacheUrl = false;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'java.png';
	public homepage = 'https://oracle.com/java/technologies/downloads';

	public async resolveDownloadUrl() {
		return ok('https://download.oracle.com/java/21/latest/jdk-21_windows-x64_bin.msi');
	}
}
