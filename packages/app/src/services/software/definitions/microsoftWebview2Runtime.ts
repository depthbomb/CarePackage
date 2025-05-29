import { ok } from 'neverthrow';
import { SoftwareCategory } from 'shared';
import type { ISoftwareDefinition } from 'shared';

export default class implements ISoftwareDefinition {
	public key = 'webview2-runtime';
	public name = 'Microsoft Edge WebView2 Runtime';
	public category = [SoftwareCategory.Runtime];
	public downloadName = 'MicrosoftEdgeWebview2Setup.exe';
	public icon = 'microsoft-edge-webview2-runtime.png';
	public homepage = 'https://developer.microsoft.com/en-us/microsoft-edge/webview2';

	public async resolveDownloadUrl() {
		return ok('https://go.microsoft.com/fwlink/p/?LinkId=2124703');
	}
}
