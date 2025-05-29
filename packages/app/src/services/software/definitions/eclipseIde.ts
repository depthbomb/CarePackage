import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'eclipse-ide';
	public name = 'Eclipse IDE';
	public category = [SoftwareCategory.Development];
	public downloadName = 'eclipse-inst-jre-win64.exe';
	public shouldCacheUrl = true;
	public icon = 'eclipse-ide.png';
	public homepage = 'https://eclipseide.org';

	public async resolveDownloadUrl() {
		const res = await fetch('https://eclipse.org/downloads/packages');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/www\.eclipse.org\/downloads\/download\.php\?file=\/oomph\/epp\/(\d{4}-\d+)\/R\/eclipse-inst-jre-win64.exe/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(`https://www.eclipse.org/downloads/download.php?file=/oomph/epp/${match[1]}/R/eclipse-inst-jre-win64.exe&r=1`);
	}
}
