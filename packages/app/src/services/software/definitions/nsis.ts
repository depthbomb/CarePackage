import { ok, err } from 'neverthrow';
import { XMLParser } from 'fast-xml-parser';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'nsis';
	public name = 'NSIS';
	public category = [SoftwareCategory.Development];
	public downloadName = 'nsis-setup.exe';
	public requiresAdmin = true;
	public icon = 'nsis.png';
	public homepage = 'https://nsis.sourceforge.io/Download';

	public async resolveDownloadUrl() {
		const downloadPageUrl = await this.getDownloadPageUrl();
		if (!downloadPageUrl) {
			return err(DownloadUrlResolveError.Generic);
		}

		const res = await fetch(downloadPageUrl);
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/<a href="(.*)" rel="nofollow">/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[1]);
	}

	private async getDownloadPageUrl() {
		const res = await fetch('https://sourceforge.net/projects/nsis/rss');
		if (!res.ok) {
			return null;
		}

		const parser       = new XMLParser();
		const xml          = await res.text();
		const data         = parser.parse(xml);
		const downloadPath = data.rss.channel.item.find(
			(i: { title: string; }) => i.title.endsWith('-setup.exe')
		).title;

		return `https://sourceforge.net/settings/mirror_choices?projectname=nsis&filename=${downloadPath}&dialog=true`;
	}
}
