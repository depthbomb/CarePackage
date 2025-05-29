import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'libreoffice';
	public name = 'LibreOffice';
	public category = [SoftwareCategory.Productivity];
	public downloadName = 'LibreOffice_Win_x86-64.msi';
	public shouldCacheUrl = true;
	public icon = 'libreoffice.png';
	public homepage = 'https://libreoffice.org';

	public async resolveDownloadUrl() {
		const version = await this.getLatestVersion();
		if (!version) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(`https://mirror.usi.edu/pub/tdf/libreoffice/stable/${version}/win/x86_64/LibreOffice_${version}_Win_x86-64.msi`);
	}

	private async getLatestVersion() {
		const res = await fetch('https://libreoffice.org/download/download-libreoffice');
		if (!res.ok) {
			null;
		}

		const html  = await res.text();
		const match = html.match(/href='\/download\/download-libreoffice\/\?type=win-x86_64&version=(\d+\.\d+\.\d)+&lang=en-US'><i class=".*"><\/i>Windows x86_64 \(Windows 7 or newer required\)/);
		if (!match) {
			return null;
		}

		return match[1];
	}
}
