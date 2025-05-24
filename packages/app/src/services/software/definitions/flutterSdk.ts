import { ok, err } from 'neverthrow';
import { SoftwareCategory, DownloadUrlResolveError } from 'shared';
import type { ISoftwareDefinition } from 'shared';

type FlutterRelease = {
	channel: string;
	archive: string;
};

export default class implements ISoftwareDefinition {
	public key = 'flutter-windows-sdk';
	public name = 'Flutter SDK';
	public category = [SoftwareCategory.Development];
	public downloadName = 'flutter_windows_stable.zip';
	public isArchive = true;
	public shouldCacheUrl = true;
	public requiresAdmin = false;
	public deprecated = false;
	public icon = 'flutter.png';
	public homepage = 'https://docs.flutter.dev';

	public async resolveDownloadUrl() {
		const res = await fetch('https://storage.googleapis.com/flutter_infra_release/releases/releases_windows.json');
		if (!res.ok) {
			return err(DownloadUrlResolveError.HTTPResponseError);
		}

		const json                = await res.json() as any;
		const releases            = json['releases'] as FlutterRelease[];
		const latestStableRelease = releases.find(r => r.channel === 'stable');
		if (!latestStableRelease) {
			return err(DownloadUrlResolveError.Generic);
		}

		return ok(`https://storage.googleapis.com/flutter_infra_release/releases/${latestStableRelease.archive}`);
	}
}
