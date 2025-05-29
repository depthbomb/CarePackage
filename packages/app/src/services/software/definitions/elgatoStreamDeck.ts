import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'elgato-stream-deck';
	public name = 'Elgato Stream Deck';
	public category = [SoftwareCategory.Peripheral];
	public downloadName = 'Stream_Deck.msi';
	public shouldCacheUrl = true;
	public icon = 'elgato-stream-deck.png';
	public homepage = 'https://help.elgato.com/hc/en-us/sections/5162671529357-Elgato-Stream-Deck-Software-Release-Notes';

	public async resolveDownloadUrl() {
		const res = await fetch('https://elgato.com/us/en/s/downloads');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const html  = await res.text();
		const match = html.match(/https:\/\/edge\.elgato\.com\/egc\/windows\/sd\/Stream_Deck_\d+\.\d+\.\d+\.\d+\.msi/);
		if (!match) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(match[0]);
	}
}
